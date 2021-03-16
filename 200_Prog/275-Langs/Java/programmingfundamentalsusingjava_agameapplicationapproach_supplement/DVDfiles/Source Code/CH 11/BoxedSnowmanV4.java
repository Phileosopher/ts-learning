  import java.awt.*;
  import javax.swing.*; 
  import java.awt.event.*;

  public class BoxedSnowmanV4 extends JPanel implements ActionListener
  {   
    private int xS = 8;
    private int yS = 30;
    private Color hatColor = Color.BLACK;
    private int dx = 0;
    private int dy = 0;
    private int time = 0;
    private Timer aTimer = new Timer(1000, this);

    public BoxedSnowmanV4(int initalX, int initalY, Color hatColor)  
    {
      xS = initalX;  
      yS = initalY;
      this.hatColor = hatColor;
      addMouseListener(new MouseHandler());
      addMouseMotionListener(new MouseHandler());
      addKeyListener(new KeyHandler());
      aTimer.start();
    }
    public void paintComponent(Graphics g)
    {   
      super.paintComponent(g);
      g.setColor(hatColor);
      g.fillRect(xS + 15, yS, 10, 15);  // hat
      g.fillRect(xS + 10, yS + 15, 20, 2);  // brim
      g.setColor(Color.WHITE);
      g.fillOval(xS + 10, yS + 17, 20, 20); // head
      g.fillOval(xS, yS + 37, 40, 40);  // body
      g.setColor(Color.RED);
      g.fillOval(xS + 19, yS + 53, 4, 4);  //button
      g.setColor(Color.BLACK);
      g.drawRect(xS, yS, 40, 77); // inscribing rectangle
      g.setFont(new Font("Sherif", Font.BOLD, 20));
      g.drawString("Time: " + time, 300, 50);
    }    
    public int getXS()
    {
      return xS;
    }
    public void setXS(int newX)
    {
     xS = newX;
    }
    public int getYS()
    {
      return yS;
    }
    public void setYS(int newY)
    {
      yS = newY;
    }
    public void actionPerformed(ActionEvent e)
    {
      time++;
      repaint();
    }
    public void addNotify()
    {
      super.addNotify();
      requestFocusInWindow();
    }
    public class KeyHandler extends KeyAdapter
    {
      public void keyPressed(KeyEvent e)
      { 
        String key = KeyEvent.getKeyText(e.getKeyCode());
        if(key.equals("Right"))
        {
          xS = xS + 3;
          repaint();
        }
      } 
    }
    public class MouseHandler extends MouseAdapter
    {
      public void mouseDragged(MouseEvent e)
      {
        xS = e.getX() - dx;
        yS = e.getY() - dy;
        repaint();
      }
      public void mousePressed(MouseEvent e)
      {
        dx = e.getX() - xS;
        dy = e.getY() - yS;
      }
      public void mouseClicked(MouseEvent e)
      {
        xS = e.getX();
        yS = e.getY();
        repaint();
      }
      public void mouseEntered(MouseEvent e)
      {
       System.out.println("Entered");
      }
       public void mouseExited(MouseEvent e)
      {
       System.out.println("Exited");
      }
    }
  }
