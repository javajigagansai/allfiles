
import java.util.Scanner;

class BinarySearch {
    public static void main(String[] args) {
        int i, mid, first, last, x, n;
        boolean found = false;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        n = sc.nextInt();

        int a[] = new int[n];

        System.out.println("Enter elements of array (in sorted order): ");
        for (i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        System.out.print("Enter element to search: ");
        x = sc.nextInt();

        first = 0;
        last = n - 1;

        while (first <= last) {
            mid = (first + last) / 2;

            if (a[mid] == x) {
                found = true;
                System.out.println("Element found at position: " + (mid + 1));
                break;
            } 
            else if (a[mid] > x) {
                last = mid - 1;
            } 
            else {
                first = mid + 1;
            }
        }

        if (!found) {
            System.out.println("Element not found");
        }
    }
}
