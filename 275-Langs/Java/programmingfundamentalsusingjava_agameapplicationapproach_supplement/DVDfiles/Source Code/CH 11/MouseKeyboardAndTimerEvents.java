  import javax.swing.*;
  import java.awt.*;

  public class MouseKeyboardAndTimerEvents extends JFrame
  {
    public static void main(String[] args) 
    { 
      JFrame window = new JFrame("MOUSE, KEYBOARD, AND TIMER EVENTS");
      window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      BoxedSnowmanV4 s1 = new BoxedSnowmanV4(315, 165, Color.BLUE);
      window.add(s1);
      window.setSize(708, 434);
      window.setVisible(true);
    }
  }
