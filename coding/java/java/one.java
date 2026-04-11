public class Billing {
    public static void main(String[] args) {
        int qty = -5;       // change and test

        try {
            if (qty <= 0)
                throw new Exception("Invalid Quantity!");
            System.out.println("Valid Quantity = " + qty);
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }
}
