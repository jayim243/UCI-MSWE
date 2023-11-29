public class TrafficController {
    private final Object sharedLock = new Object(); //shared lock between all functions: only one function can work at a time
    private boolean carEntering = false; //bool to know when a car is on the bridge


    public void enterLeft() {
        synchronized (sharedLock) {
            try {
                while (carEntering) { //if a car is on the bridge, wait
                    sharedLock.wait();
                }
                carEntering = true; //once a car leaves the bridge, it will set carEntering to false, so once this car enters, we set it to true again
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
    public void enterRight() {
        synchronized (sharedLock) {
            try {
                while (carEntering) { //if a car is on the bridge, wait
                    sharedLock.wait();
                }
                carEntering = true; //once a car leaves the bridge, it will set carEntering to false, so once this car enters, we set it to true again
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
    public void leaveLeft() {
        synchronized (sharedLock) {
            carEntering = false; //car left bridge
            sharedLock.notifyAll();  // Notify all waiting threads
        }
    }
    public void leaveRight() {
        synchronized (sharedLock) {
            carEntering = false; //car left bridge
            sharedLock.notifyAll();  // Notify all waiting threads
        }
    }
}