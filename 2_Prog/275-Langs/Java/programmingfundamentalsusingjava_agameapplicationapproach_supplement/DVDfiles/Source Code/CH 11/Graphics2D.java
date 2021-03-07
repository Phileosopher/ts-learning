  import javax.swing.*;
  import java.awt.*;

  public class Graphics2D extends JFrame
  {
    public static void main(String[] args) 
    { 
      JFrame window = new JFrame("Graphics");
      window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      BoxedSnowmanV3 s1 = new BoxedSnowmanV3(315, 165, Color.BLUE);
      window.add(s1);
      window.setSize(708, 434);
      window.setVisible(true);
    }
  }
