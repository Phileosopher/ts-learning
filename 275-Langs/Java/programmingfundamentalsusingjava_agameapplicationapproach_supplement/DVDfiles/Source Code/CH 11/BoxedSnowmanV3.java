  import java.awt.*;
  import javax.swing.*; 

  public class BoxedSnowmanV3 extends JPanel 
  {   
    private int x = 8;
    private int y = 30;
    private Color hatColor = Color.BLACK;
    private int dx = 0;
    private int dy = 0;
    private int time = 0;

    public BoxedSnowmanV3(int initalX, int initalY, Color hatColor)  
    {
      x = initalX;  
      y = initalY;
      this.hatColor = hatColor;
    }
    public void paintComponent(Graphics g)
    {   
      super.paintComponent(g);
      g.setColor(hatColor);
      g.fillRect(x + 15, y, 10, 15); //hat
      g.fillRect(x + 10, y + 15, 20, 2); //brim
      g.setColor(Color.WHITE);
      g.fillOval(x + 10, y + 17, 20, 20); //head
      g.fillOval(x, y + 37, 40, 40); //body
      g.setColor(Color.RED);
      g.fillOval(x + 19, y + 53, 4, 4); //button
      g.setColor(Color.BLACK);
      g.drawRect(x, y, 40, 77); //inscribing rectangle
      g.setFont(new Font("Sherif", Font.BOLD, 20)); //time
      g.drawString("Time: " + time, 300, 50);
    }
    public int getXS()
    {
      return x;
    }
    public void setXS(int newX)
    {
      x = newX;
    }
    public int getYS()
    {
      return y;
    }
    public void setYS(int newY)
    {
      y = newY;
    }
  }  
