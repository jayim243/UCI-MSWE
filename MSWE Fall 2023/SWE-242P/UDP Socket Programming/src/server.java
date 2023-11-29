import java.io.*;
import java.net.*;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.regex.*;

public class server {
    public static void main(String[] args) {
        System.out.println("in terminal cd to src, javac server and client, java server directory, java client command portnum");
        String directory = args[0];
        int portNumber = Integer.parseInt(args[1]);
        ExecutorService threadPool = Executors.newCachedThreadPool();

        try (DatagramSocket socket = new DatagramSocket(portNumber)) {
            // printing connected status on the server side
            System.out.println("Server directory: " + directory);
            System.out.println("Server listening on port: " + portNumber);
            while (true) {
                byte[] data = new byte[8192];
                DatagramPacket packet = new DatagramPacket(data, data.length);
                socket.receive(packet);

                // Handle each request in a separate thread using the thread pool
                threadPool.submit(new HandleRequest(socket, packet, directory));
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            threadPool.shutdown();
        }
    }

    private static class HandleRequest implements Runnable {
        private DatagramSocket socket;
        private DatagramPacket packet;
        private String directory;
        private static Map<Integer, byte[]> dataChunks = new HashMap<>(); // map to hold all corresponding sequence numbers and their bytes

        public HandleRequest(DatagramSocket socket, DatagramPacket packet, String directory) {
            this.socket = socket;
            this.packet = packet;
            this.directory = directory;
        }



        @Override
        public void run() {
            try {
                String clientCommand = new String(packet.getData(), 0, packet.getLength());
                System.out.println("Received from client: " + clientCommand);

                if (clientCommand.equals("shutdown")) {
                    try {
                        sendResponse("Server is shutting down...", packet.getAddress(), packet.getPort());
                        socket.close();
                    } catch (SocketException e) {
                        System.err.println("Server shut down by the client");
                    }
                } else if (clientCommand.equals("index")) {
                    try {
                        sendFileList(packet.getAddress(), packet.getPort());
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                } else if (clientCommand.startsWith("retransmit ")) {
                    handleRetransmission(clientCommand);
                } else if (clientCommand.startsWith("get") && clientCommand.endsWith(".txt")) {
                    handleGetCommand(clientCommand);
                } else {
                    sendResponse("error: only commands are: \"index\" or \"get <txt file>\"", packet.getAddress(), packet.getPort());
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }


        private byte[] getRetransmissionData(int sequenceNumber) {
            return dataChunks.get(sequenceNumber);
        }

        private void handleRetransmission(String clientCommand) throws IOException {
            String[] parts = clientCommand.split(" ", 3);
            int sequenceNumber = Integer.parseInt(parts[1]);

            byte[] retransmissionData = getRetransmissionData(sequenceNumber);

            DatagramPacket retransmissionPacket = new DatagramPacket(retransmissionData, retransmissionData.length, packet.getAddress(), packet.getPort());
            socket.send(retransmissionPacket);
        }

        private void handleGetCommand(String clientCommand) throws IOException, InterruptedException {
            String fileName = clientCommand.substring(4);
            Path filePath = Paths.get(directory, fileName);

            int sequenceNumber = 0;
            if (Files.exists(filePath) && Files.isRegularFile(filePath)) {
                byte[] ok = (sequenceNumber + " ok").getBytes();
                dataChunks.put(sequenceNumber, " ok".getBytes());
                DatagramPacket send = new DatagramPacket(ok, ok.length, packet.getAddress(), packet.getPort());
                socket.send(send);
                sequenceNumber++;


                try (DataInputStream fileReader = new DataInputStream(new FileInputStream(filePath.toFile()))) {
                    byte[] buffer = new byte[8192];
                    int bytesRead;

                    while ((bytesRead = fileReader.read(buffer)) != -1) {
                        sendFileChunk(buffer, bytesRead, sequenceNumber, packet.getAddress(), packet.getPort());
                        sequenceNumber++;
                        Thread.sleep(10);  // Introduce a small delay to simulate network latency
                    }
                    sendFileEnd(packet.getAddress(), packet.getPort());
                }
            } else {
                byte[] error = (sequenceNumber + " error").getBytes();
                DatagramPacket send = new DatagramPacket(error, error.length, packet.getAddress(), packet.getPort());
                socket.send(send);
                dataChunks.put(sequenceNumber, " error".getBytes());
                sendFileEnd(packet.getAddress(), packet.getPort());
            }
//            for (Map.Entry<Integer, byte[]> entry : dataChunks.entrySet()) {
//                int key = entry.getKey();
//                byte[] value = entry.getValue();
//
//                System.out.println("Key: " + key + ", Value: " + value.toString());
//            }
        }


        private void sendFileList(InetAddress clientAddress, int clientPort) throws IOException {
            try (DirectoryStream<Path> directoryStream = Files.newDirectoryStream(Paths.get(directory))) {
                for (Path path : directoryStream) {
                    if (Files.isRegularFile(path)) {
                        sendResponse(path.getFileName().toString(), clientAddress, clientPort);
                    }
                }
                sendResponse("end", clientAddress, clientPort);
            }
        }

        private void sendFileChunk(byte[] data, int length, int sequenceNumber, InetAddress clientAddress, int clientPort) throws IOException {
            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
            DataOutputStream dataOutputStream = new DataOutputStream(byteArrayOutputStream);


            dataOutputStream.write((sequenceNumber + " ").getBytes());

            dataOutputStream.write(data, 0, length);

            byte[] packetData = byteArrayOutputStream.toByteArray();
            DatagramPacket sendPacket = new DatagramPacket(packetData, packetData.length, clientAddress, clientPort);
            byte[] dataChunk = Arrays.copyOf(packetData, packetData.length);
            dataChunks.put(sequenceNumber, dataChunk);
            socket.send(sendPacket);
        }

        private void sendFileEnd(InetAddress clientAddress, int clientPort) throws IOException {
            byte[] endData = "end".getBytes();
            DatagramPacket endPacket = new DatagramPacket(endData, endData.length, clientAddress, clientPort);
            socket.send(endPacket);
        }

        private void sendResponse(String str, InetAddress clientAddress, int clientPort) throws IOException {
            byte[] data = str.getBytes();
            DatagramPacket send = new DatagramPacket(data, data.length, clientAddress, clientPort);
            socket.send(send);
        }
    }
}