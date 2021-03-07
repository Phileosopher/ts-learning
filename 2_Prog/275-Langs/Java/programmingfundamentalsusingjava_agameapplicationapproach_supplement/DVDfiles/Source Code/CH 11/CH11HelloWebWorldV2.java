  import java.awt.*;
  import javax.swing.*;

  public class CH11HelloWebWorldV2 extends JApplet 
  {
    GraphicsPanel aPanel;

    public void init() 
    {
      aPanel = new GraphicsPanel();
      add(aPanel);
    }
  }
