

// First thread class
class A extends Thread {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Thread A: " + i);
            try {
                Thread.sleep(500); // pause for 0.5 seconds
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

// Second thread class
class B extends Thread {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Thread B: " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

// Main class
public class MultiThreadExample {
    public static void main(String[] args) {
        A t1 = new A(); // create first thread
        B t2 = new B(); // create second thread

        t1.start(); // start first thread
        t2.start(); // start second thread
    }
}
