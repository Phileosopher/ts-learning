  import java.awt.*;
  import java.applet.*;

  public class CH11HelloWebWorld extends Applet 
  {
    public void paint(Graphics g) 
    { 
      super.paint(g);
      g.setFont(new Font("Sherif", Font.BOLD, 16));
      g.drawString("Hello Web World", 170, 130 );
      g.setColor(Color.BLUE);
      g.fillOval(200, 140, 70, 70);
    }
  }
