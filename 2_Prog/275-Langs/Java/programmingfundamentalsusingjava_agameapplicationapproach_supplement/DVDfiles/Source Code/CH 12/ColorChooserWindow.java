  import javax.swing.*;
  import java.awt.Color;

  public class ColorChooserWindow extends JFrame
  {
    public ColorChooserWindow(String title) 
    {
      super(title);
      setSize(400, 300);

      JPanel aPanel = new JPanel();
      Color aColor;

      //Obtain the background color of the window
      aColor = JColorChooser.showDialog(null, "Choose the Window's color",
                                        Color.BLACK);
      aPanel.setBackground(aColor);
      add(aPanel);
    }
  }
