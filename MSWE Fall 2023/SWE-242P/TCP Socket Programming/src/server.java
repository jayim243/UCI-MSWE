import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class server {
    private static volatile boolean isShuttingDown = false;
    public static void main(String[] args) throws IOException {
        System.out.println("in terminal cd to src, javac server and client, java server directory, java client command portnum");
        String directory = args[0];
        int portNumber = Integer.parseInt(args[1]);
        ExecutorService threadPool = Executors.newCachedThreadPool();
        try (
                ServerSocket serverSocket = new ServerSocket(portNumber);

        ) {
            // printing connected status on server side
            System.out.println("Server directory: " + directory);
            System.out.println("Server listening on port: " + portNumber);
            while (true) {
                Socket clientSocket = serverSocket.accept();
                threadPool.submit(new handleRequest(clientSocket, directory));
                if (isShuttingDown) {
                    break;
                }
            }
        }
        threadPool.shutdown();
    }


    private static class handleRequest implements Runnable {
        private Socket clientSocket;
        private String directory;

        public handleRequest(Socket clientSocket, String directory) {
            this.clientSocket = clientSocket;
            this.directory = directory;
        }
        @Override
        public void run() {
            try (
                    PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                    BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            ) {
                String clientCommand = in.readLine();
                if (clientCommand.equals("shutdown")) {
                    out.println("Server is shutting down");
                    isShuttingDown = true;
                    clientSocket.close();
                    return; //exit thread immediately
                }


                if (clientCommand.equals("index")) {
//                chatGPT to list files given directory name
                    try (DirectoryStream<Path> directoryStream = Files.newDirectoryStream(Paths.get(directory))) {
                        for (Path path : directoryStream) {
                            if (Files.isRegularFile(path)) {
                                out.println(path.getFileName());
                            }
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }



                else if (clientCommand.length() >= 3 && clientCommand.startsWith("get") && clientCommand.endsWith(".txt")) {
                    if (clientCommand.length() == 3) {
                        out.println("error: provide a file name");
                        clientSocket.close();
                    }

                    String fileName = clientCommand.substring(4);
                    boolean exists = false;
                    try (DirectoryStream<Path> directoryStream = Files.newDirectoryStream(Paths.get(directory))) {
                        for (Path path : directoryStream) {
                            if (Files.isRegularFile(path) && !exists) {
                                if (path.getFileName().toString().equals(fileName)) {
                                    out.println("ok");
                                    exists = true;

                                    try (BufferedReader fileReader = Files.newBufferedReader(path)) {
                                        String line;
                                        while ((line = fileReader.readLine()) != null) {
                                            out.println(line);
                                        }
                                    }
                                }
                            }
                        }
                        if (!exists) {
                            out.println("error");
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    } finally {
                        // close connection regardless. closing socket closes in/out streams
                        clientSocket.close();
                    }
                }


                else {
                    out.println("error: only commands are: \"index\" or \"get <txt file>\"");
                    clientSocket.close();
                }

            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}