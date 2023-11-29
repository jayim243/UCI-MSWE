import java.io.IOException;
import java.net.*;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.*;

public class client {
    private static final String GET_COMMAND_PATTERN = "^get\\s+(.+\\.txt)$"; // chatGPT: regex to validate get .txt files

    public static void main(String[] args) {
        System.out.println("in terminal cd to src, javac server and client, java server directory, java client command portnum");
        try {
            if (args.length == 2 && (args[0].equals("index") || args[0].equals("shutdown"))) {
                // "index" command
                String command = args[0];
                int portNumber = Integer.parseInt(args[1]);
                receiveFile(command, portNumber);
            } else if (isValidGetCommand(args[0] + " " + args[1])) {
                // "get <txt file>" command
                String command = args[0] + " " + args[1];
                int portNumber = Integer.parseInt(args[2]);
                receiveFile(command, portNumber);
            } else {
                System.out.println("Invalid arguments");
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid port number. Please provide a valid integer port number.");
        } catch (IOException e) {
            System.out.println("Error during communication with the server: " + e.getMessage());
        }
    }


    // chatGPT: regex to validate get .txt files
    public static boolean isValidGetCommand(String command) {
        Pattern pattern = Pattern.compile(GET_COMMAND_PATTERN);
        Matcher matcher = pattern.matcher(command);

        return matcher.matches();
    }

    private static void receiveFile(String command, int portNumber) throws IOException {
        try (DatagramSocket socket = new DatagramSocket()) {
            socket.setSoTimeout(10000);
            InetAddress host = InetAddress.getByName("localhost");

            // Send the "get <filename>" command to the server for "get" command
            byte[] data = command.getBytes();
            DatagramPacket packet = new DatagramPacket(data, data.length, host, portNumber);
            socket.send(packet);

            receiveResponse(command, socket, host, portNumber);
        }
    }

    private static void receiveResponse(String command, DatagramSocket socket, InetAddress host, int portNumber) throws IOException {
        byte[] receiveData = new byte[8192];
        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

        if (command.equals("shutdown")) {
            socket.receive(receivePacket);
            String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println(response);
        } else if (command.equals("index")) {
            while (true) {
                socket.receive(receivePacket);
                String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
                if (response.equals("end")) {
                    break;
                }
                System.out.println(response);
            }
        } else if (command.startsWith("get")) {
            Map<Integer, String> receivedChunks = new HashMap<>(); // holds all messages; loop through them to see if we are missing any
            int expectedSequenceNumber = 0;
            while (true) {
                socket.receive(receivePacket);
                String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
                if (response.equals("end")) {
                    break;
                }
                String[] parts = response.split(" ", 2);
                if (expectedSequenceNumber == Integer.parseInt(parts[0])) {
                    receivedChunks.put(expectedSequenceNumber, parts[1]);
                    System.out.println("sequenceNumber: " + parts[0] + " response: " + parts[1]);
                    expectedSequenceNumber++;
                } else {
                    int retransmissionSequenceNumber = Integer.parseInt(response.split(" ")[0]);
                    System.out.println("retransmission needed for:" + retransmissionSequenceNumber);
                    sendRetransmissionRequest(Integer.parseInt(parts[0]), command.split(" ", 2)[1], socket, host, portNumber);
                    DatagramPacket retransmissionResponsePacket = receiveRetransmissionResponse(socket);

                    // processing retransmissionResponsePacket
                    String responseString = new String(retransmissionResponsePacket.getData(), 0, retransmissionResponsePacket.getLength());
                    String[] parts2 = responseString.split(" ", 2);
                    while (Integer.parseInt(parts2[0]) != retransmissionSequenceNumber) { // keep trying retransmission til its correct
                        System.out.println("retransmission needed for:" + retransmissionSequenceNumber);
                        sendRetransmissionRequest(Integer.parseInt(parts[0]), command.split(" ", 2)[1], socket, host, portNumber);
                        retransmissionResponsePacket = receiveRetransmissionResponse(socket);

                        // processing retransmissionResponsePacket
                        responseString = new String(retransmissionResponsePacket.getData(), 0, retransmissionResponsePacket.getLength());
                        parts2 = responseString.split(" ", 2);
                    }
                    receivedChunks.put(Integer.valueOf(parts2[0]), parts2[1]); // finally adding retransmission to map
                    expectedSequenceNumber++;
                }
            }
        }
    }

    private static void sendRetransmissionRequest(int sequenceNumber, String fileName, DatagramSocket socket, InetAddress host, int portNumber) throws IOException {
        String request = "retransmit " + sequenceNumber + " " + fileName;
        byte[] requestData = request.getBytes();

        DatagramPacket requestPacket = new DatagramPacket(requestData, requestData.length, host, portNumber);
        socket.send(requestPacket);
    }


    private static DatagramPacket receiveRetransmissionResponse(DatagramSocket socket) throws IOException {
        byte[] buffer = new byte[8192];
        DatagramPacket responsePacket = new DatagramPacket(buffer, buffer.length);

        socket.receive(responsePacket);

        return responsePacket;
    }
}