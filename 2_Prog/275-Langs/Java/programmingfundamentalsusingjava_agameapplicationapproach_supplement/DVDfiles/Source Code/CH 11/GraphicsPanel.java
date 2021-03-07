  import java.awt.*;
  import javax.swing.*;

  public class GraphicsPanel extends JPanel
  {
    public void paintComponent(Graphics g)
    {
      super.paintComponent(g);
      g.setFont(new Font("Sherif", Font.BOLD, 16));
      g.drawString("Hello Web World", 170, 130 );
      g.setColor(Color.BLUE);
      g.fillOval(200, 140, 70, 70);
    }
  }
