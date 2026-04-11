
import java.io.*;
import java.awt.*;
 import java.applet.*;
import java.awt.event.*;
/*
<applet code="carddemo" width=250 height=150>
</applet>
*/

public class carddemo extends Applet implements ActionListener
{
Button b1,b2,b3,b4; Panel buttonPanel;
CardLayout buttonCardLayout; public void init()
{
buttonPanel=new Panel(); add(buttonPanel); buttonCardLayout=new CardLayout();
buttonPanel.setLayout(buttonCardLayout); b1=new Button("first Button"); b1.addActionListener(this); buttonPanel.add(b1,"first Button"); b2=new Button("second Button"); b2.addActionListener(this); buttonPanel.add(b2,"second Button"); b3=new Button("third button"); b3.addActionListener(this); buttonPanel.add(b3,"third Button");
}
public void actionPerformed(ActionEvent e)
{
buttonCardLayout.next(buttonPanel);
}
}
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

/*
<applet code="carddemo.class" width="300" height="200"></applet>
*/

public class carddemo extends Applet implements ActionListener {

    Button b1, b2, b3;
    Panel buttonPanel;
    CardLayout cardLayout;

    public void init() {

        cardLayout = new CardLayout();
        buttonPanel = new Panel();
        buttonPanel.setLayout(cardLayout);

        b1 = new Button("First Button");
        b1.addActionListener(this);

        b2 = new Button("Second Button");
        b2.addActionListener(this);

        b3 = new Button("Third Button");
        b3.addActionListener(this);

        buttonPanel.add("1", b1);
        buttonPanel.add("2", b2);
        buttonPanel.add("3", b3);

        add(buttonPanel);
    }

    public void actionPerformed(ActionEvent e) {
        cardLayout.next(buttonPanel);
    }
}
