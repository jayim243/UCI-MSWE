import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Thread> threadList = new ArrayList<>(); //arraylist to store threads, allows us to easily stop a thread given user input "b"
        int threadNum = 1;

        Scanner scanner = new Scanner(System.in);
        String[] parts;
        String[] validParts = {"a", "b", "c"}; //to validate parts[0] is follows our options
        boolean found = false; //bool to ensure parts[0] in validParts
        while (true) { //repeat program until "c"
            String input;
            do {
                System.out.println("Here are your options: \n" +
                        "a - Create a new thread \n" +
                        "b - Stop a given thread (e.g. \"b 2\" kills thread 2) \n" +
                        "c - Stop all threads and exit this program.\n");
                input = scanner.nextLine();
                parts = input.split(" "); //splits input to handle case b

                if (input.trim().isEmpty()) { //if user input are empty spaces, prompt new input
                    System.out.println("Input should not be just an empty space. Please provide valid input.");
                    continue;
                }
                if (parts.length > 2) { //if array > 2 that means input have at least 3 characters, prompt new input
                    System.out.println("Input should not exceed 3 arguments. Please give a valid input from the options");
                    continue;
                }
                for (String s : validParts) { //ensures part[0] is in [a, b, c], if not, prompt new input
                    if (parts[0].equals(s)) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    System.out.println("Input should start with a, b, or c. Please give a valid input from the options");
                    continue;
                }
                if ((parts.length >= 2 && (parts[0].equals("a") || parts[0].equals("c")))) { //ensures that inputs a or c have no additional arguments, if not, prompt new input
                    System.out.println("Invalid input. Please provide a valid option.");
                    continue;
                }
            } while (input.trim().isEmpty() || parts.length > 2 || !found || (parts.length >= 2 && (parts[0].equals("a") || parts[0].equals("c")))); //keep repeating while any of these conditions exist

            switch (parts[0]) { //looking at what letter the user input begins with
                case "a" -> {
                    MyRunnable hello = new MyRunnable(threadNum); //create MyRunnable obj with thread number that will increment each time a new object is created
                    threadNum++;
                    Thread myThread = new Thread(hello); //passes MyRunnable obj to Thread obj to create a new thread
                    threadList.add(myThread); //add thread to arraylist
                    myThread.start(); //start the thread
                    System.out.println(threadList); //print arraylist to visualize better
                }
                case "b" -> {
                    if (parts.length == 1) { //if user does not specify what thread to stop
                        System.out.println("Please specify a thread to stop");
                    } else {
                        int threadIndex = Integer.parseInt(parts[1]) - 1; //1-based index arraylist: index to retrieve correct thread from arraylist to stop
                        if (threadList.size() <= threadIndex) { //edge case if user tries to stop thread number that is greater than all the threads we currently have
                            System.out.println("There is currently no thread by that index");
                        } else {
                            threadList.get(threadIndex).interrupt(); //gets thread object from arraylist and interrupts it
                            threadList.remove(threadIndex); //remove thread from arraylist to keep it "updated"
                            System.out.println("Thread" + (threadIndex + 1) + "successfully removed"); //print output
                        }
                    }
                }
                case "c" -> {
                    for (Thread thread : threadList) { //loop through arraylist and stops them all
                        thread.interrupt();
                    }
                    threadList.clear(); //clear arraylist, fully stopping all threads
                    System.exit(0); //exit program
                }
            }
        }
    }
}