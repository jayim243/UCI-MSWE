import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.*;

public class exerciseM2 {
    public static void main(String[] args) {
        System.out.println("How to use: move to src folder and make sure all txt files are in src folder, run javac exerciseM2.java to compile program, then run java exerciseM2.java file1.txt file2.txt ...");
    // calling from command line breaks input into array of strings which is passed as args
        for (String fileName: args) {
            Path filePath = Paths.get(fileName);
            if (Files.exists(filePath) && Files.isRegularFile(filePath)) {
                System.out.println(fileName + ": " + countLines(fileName));
            } else {
                System.err.println("Error reading from file " + fileName);
            }
        }
    }


    private static int countLines(String fileName) {
        int lines = 0;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            while (reader.readLine() != null) {
                lines++;
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return lines;
    }
}