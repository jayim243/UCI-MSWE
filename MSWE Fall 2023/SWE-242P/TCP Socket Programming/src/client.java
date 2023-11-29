import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class client {
    private static final String GET_COMMAND_PATTERN = "^get\\s+(.+\\.txt)$"; // chatGPT: regex to validate get .txt files
    public static void main(String[] args) {
        System.out.println("in terminal cd to src, javac server and client, java server directory, java client command portnum");
        try {
            String command;
            int portNumber;
            if (args.length == 2 && args[0].equals("index")) { // for "index"
                command = args[0];
                portNumber = Integer.parseInt(args[1]);

                try (
                        Socket socket = new Socket("localhost", portNumber);
                        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                ) {
                    out.println(command);
                    out.println(portNumber);

                    String line;
                    while ((line = in.readLine()) != null) {
                        System.out.println(line);
                    }
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }


            } else if (isValidGetCommand(args[0] + " " + args[1])) { // for "get <txt file>"
                command = args[0];
                String fileName = args[1];
                portNumber = Integer.parseInt(args[2]);

                try (
                        Socket socket = new Socket("localhost", portNumber);
                        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                ) {
                    out.println(command + " " + fileName);
                    out.println(portNumber);

                    String line;
                    while ((line = in.readLine()) != null) {
                        System.out.println(line);
                    }
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            } else {
                System.out.println("Invalid arguments");
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid port number. Please provide a valid integer port number.");
        }
    }

    // chatGPT: regex to validate get .txt files
    public static boolean isValidGetCommand(String command) {
        Pattern pattern = Pattern.compile(GET_COMMAND_PATTERN);
        Matcher matcher = pattern.matcher(command);

        return matcher.matches();
    }
}
