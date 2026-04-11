

import java.util.Scanner;

public class ExceptionExample {

    // This method declares that it might throw an exception
    static void divide(int a, int b) throws ArithmeticException {
        if (b == 0) {
            // We manually throw an exception
            throw new ArithmeticException("Cannot divide by zero!");
        } else {
            System.out.println("Result = " + (a / b));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter first number: ");
            int x = sc.nextInt();

            System.out.print("Enter second number: ");
            int y = sc.nextInt();

            // calling the method which may throw an exception
            divide(x, y);
        } 
        catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } 
        finally {
            System.out.println("Program finished safely.");
        }

        sc.close();
    }
}
