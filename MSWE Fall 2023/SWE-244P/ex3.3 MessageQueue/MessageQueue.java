import java.util.ArrayList;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

public class MessageQueue {
	private static int n_ids;
    private static ArrayList<Producer> myProducers = new ArrayList<>();

	public static void main(String[] args) {
		BlockingQueue<Message> queue = new ArrayBlockingQueue<>(10); //use BlockingQueue so threads can block when enqueueing ande dequeueing messages
//		Producer p1 = new Producer(queue, n_ids++);
//		Consumer c1 = new Consumer(queue, n_ids++);
//		Producer p2 = new Producer(queue, n_ids++); //second producer
//		Consumer c2 = new Consumer(queue, n_ids++); //second consumer
//
//		new Thread(p1).start();
//		new Thread(c1).start();
//		new Thread(p2).start(); //second producer thread
//		new Thread(c2).start(); //second consumer thread
        System.out.println("How to use: create java class initialization by using javac Producer.java, javac consumer.java, javac MessageQueue.java");
        System.out.println("java MessageQueue.java <numProducers> <numConsumers>");
        if (args.length != 2) {
            System.out.println("How to use: create java class initialization by using javac Producer.java, javac consumer.java, javac MessageQueue.java");
            System.out.println("java MessageQueue.java <numProducers> <numConsumers>");
            System.exit(1);
        }

        //CL inputs
        int numProducers = Integer.parseInt(args[0]);
        int numConsumers = Integer.parseInt(args[1]);

        // Create and start producer threads
        for (int i = 0; i < numProducers; i++) {
            Producer producer = new Producer(queue, n_ids++);
            myProducers.add(producer);
            new Thread(producer).start();
        }

        // Create and start consumer threads
        for (int i = 0; i < numConsumers; i++) {
            Consumer consumer = new Consumer(queue, n_ids++);
            new Thread(consumer).start();
        }

		try {
			Thread.sleep(10000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

        for (Producer p: myProducers) {
            p.stop();
        }
	}
}
