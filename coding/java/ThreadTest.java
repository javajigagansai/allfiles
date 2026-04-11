
public class ThreadTest {
    static class A extends Thread {
        @Override
        public void run() {
            for (int i = 1; i <= 5; i++) {
                if (i == 1) Thread.yield(); // politely give other threads a chance
                System.out.println("from thread A i=" + i);
            }
            System.out.println("exit from A");
        }
    }

    static class B extends Thread {
        @Override
        public void run() {
            for (int j = 1; j <= 5; j++) {
                System.out.println("from thread B j=" + j);
                if (j == 3) {
                    System.out.println("exit from B");
                    return; // safely stop thread B
                }
            }
            System.out.println("B finished normally");
        }
    }

    static class C extends Thread {
        @Override
        public void run() {
            for (int k = 1; k <= 5; k++) {
                System.out.println("thread C =" + k);
                if (k == 1) {
                    try {
                        Thread.sleep(1500); // sleep 1.5 seconds
                    } catch (InterruptedException e) {
                        System.out.println("C was interrupted");
                        return;
                    }
                }
            }
            System.out.println("exit from C");
        }
    }

    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        C c = new C();

        System.out.println("Start thread A");
        a.start();
        b.start();
        c.start();

        System.out.println("exit from main thread");
    }
}
