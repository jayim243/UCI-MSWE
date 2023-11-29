import java.time.LocalTime;

public class MyRunnable implements Runnable {
    final int threadNum;
    public MyRunnable (int threadNum) { //constructor to set initialize new thread's number
        this.threadNum = threadNum;
    }

    @Override
    public synchronized void run() {
        while (true) {
            System.out.println("Hello World! I'm thread " + threadNum + ". The time is " + LocalTime.now());
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

    }
}

