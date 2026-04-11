
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CardDemoSwing {

    private static void createAndShowGui() {
        JFrame frame = new JFrame("CardLayout Demo - Swing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(320, 220);
        frame.setLocationRelativeTo(null);

        CardLayout cardLayout = new CardLayout();
        JPanel cardPanel = new JPanel(cardLayout);

        JButton b1 = new JButton("First Button");
        JButton b2 = new JButton("Second Button");
        JButton b3 = new JButton("Third Button");

        // Add buttons as separate "cards"
        cardPanel.add(b1, "1");
        cardPanel.add(b2, "2");
        cardPanel.add(b3, "3");

        // single ActionListener to flip cards
        ActionListener al = e -> cardLayout.next(cardPanel);

        b1.addActionListener(al);
        b2.addActionListener(al);
        b3.addActionListener(al);

        frame.getContentPane().add(cardPanel);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(CardDemoSwing::createAndShowGui);
    }
}
