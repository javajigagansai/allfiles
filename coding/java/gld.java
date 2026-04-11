
import java.awt.*;
 import java.io.*;
import java.applet.Applet.*;
 import java.applet.*;

/*<applet code="gld.class" height=300 width=300>
</applet>*/



public class gld extends Applet
{
public void init()
{
setLayout(new GridLayout(5,2));
 Button b1=new Button("A");
 Button b2=new Button("B");
 Button b3=new Button("C");
 Button b4=new Button("D");
 Button b5=new Button("E");
 Button b6=new Button("F");
 Button b7=new Button("G");
 Button b8=new Button("H");
 Button b9=new Button("I");
 Button b10=new Button("J");
 add(b1);
add(b2);
add(b3);
add(b4);
add(b5);
add(b6);
add(b7);
add(b8);
add(b9);
add(b10);
}
public Insets getInsets()
{
return new Insets(20,20,20,20);
}}
