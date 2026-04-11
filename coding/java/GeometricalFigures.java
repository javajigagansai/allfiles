

import java.applet.Applet;
import java.awt.*;

/*
<applet code="GeometricalFigures.class" width="400" height="300">
</applet>
*/

public class GeometricalFigures extends Applet {
    public void paint(Graphics g) {
        // Rectangle
        g.drawRect(50, 50, 100, 60);

        // Circle
        g.drawOval(200, 50, 60, 60);

        // Line
        g.drawLine(50, 150, 150, 200);

        // Filled Rectangle
        g.setColor(Color.blue);
        g.fillRect(250, 150, 80, 50);

        // Filled Oval
        g.setColor(Color.red);
        g.fillOval(100, 220, 60, 60);

        g.setColor(Color.black);
        g.drawString("Simple Geometrical Figures", 100, 20);
    }
}
