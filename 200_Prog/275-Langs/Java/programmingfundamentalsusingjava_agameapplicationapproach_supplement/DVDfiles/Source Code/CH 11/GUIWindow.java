  import javax.swing.*; 
  import java.awt.Color;

  public class GUIWindow 
  {
    public static void main(String[] args) 
    {
      JFrame appWindow = new JFrame("A GUI Window");
      appWindow.setSize(708, 434);
      appWindow.setLocation(100, 100);
      appWindow.getContentPane().setBackground(Color.PINK);
      appWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      appWindow.setVisible(true);
    }
  }
