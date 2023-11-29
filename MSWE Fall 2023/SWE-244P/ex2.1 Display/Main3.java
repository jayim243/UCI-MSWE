import java.util.concurrent.*;


public class Main3 {

    private static void nap(int millisecs) {
        try {
            Thread.sleep(millisecs);
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    private static void addProc(HighLevelDisplay d) {
        for (int i = 0; i < 10; i++) {
            d.addRow("ROW " + i);
            nap(500);  // Sleep for a 0.5 sec
        }
        // Add a sequence of addRow operations with short random naps.

    }

    private static void deleteProc(HighLevelDisplay d) {
        for (int i = 0; i < 10; i++) {
            nap(2000);  // Sleep for 1 second
            d.deleteRow(0);
        }
        // Add a sequence of deletions of row 0 with short random naps.
    }

    public static void main(String [] args) {
        final HighLevelDisplay d = new JDisplay2();

        new Thread () {
            public void run() {
                addProc(d);
            }
        }.start();


        new Thread () {
            public void run() {
                deleteProc(d);
            }
        }.start();

    }
}