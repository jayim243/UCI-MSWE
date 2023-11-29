import java.util.concurrent.*;


public class Main3 {
    private static final Semaphore sem = new Semaphore(1);

    private static void nap(int millisecs) {
        try {
            Thread.sleep(millisecs);
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    private static void addProc(HighLevelDisplay d) throws InterruptedException {
        for (int i = 0; i < 10; i++) {
            try {
                sem.acquire();
                d.addRow("ROW " + i);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                sem.release();
            }
            nap(500);
        }
        // Add a sequence of addRow operations with short random naps.

    }

    private static void deleteProc(HighLevelDisplay d) throws InterruptedException {
        for (int i = 0; i < 10; i++) {
            nap(2000);
            try {
                sem.acquire();
                d.deleteRow(0);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                sem.release();
            }
        }
        // Add a sequence of deletions of row 0 with short random naps.
    }

    public static void main(String [] args) {
        final HighLevelDisplay d = new JDisplay2();

        new Thread () {
            public void run() {
                try {
                    addProc(d);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        }.start();


        new Thread () {
            public void run() {
                try {
                    deleteProc(d);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        }.start();

    }
}