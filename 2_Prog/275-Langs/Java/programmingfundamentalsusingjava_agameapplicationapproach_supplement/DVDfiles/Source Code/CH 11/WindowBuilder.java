  import javax.swing.*; 
  import java.awt.*;

  public class WindowBuilder extends JFrame
  {
    public WindowBuilder(String title) 
    {
      super(title);

      setSize(708, 434);
      setLocation(100, 100);
      getContentPane().setBackground(Color.PINK);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setVisible(true);
    }
  }
