  import java.awt.*;

  public class BoxedSnowman2 
  {
    private int x = 8;
    private int y = 30;
    private Color hatColor = Color.BLACK;

    public BoxedSnowman2(int intialX, int intialY, Color hatColor)   
    {
      try
      { setX(intialX); //x = intialX;  
        setY(intialY); //y = intialY;
      }
      finally
      {
      }	
      this.hatColor = hatColor;
    }
    public void show(Graphics g) //g is the game board object
    {   
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
    }
    public int getX()
    {
      return x;
    }
    public void setX(int newX) 
    {
      if(newX > 460)
      {
        throw new RuntimeException("x is beyond the board's RIGHT");
      }
      if(newX < 6)
      {
        throw new RuntimeException("x is beyond the board's LEFT");
      }
      x = newX;
    }    
    public int getY()
    {
      return y;
    }
    public void setY(int newY)
    {
      if(newY < 30)
      {
        throw new RuntimeException("y is beyond the board's TOP");
      }
      if(newY > 423)
      {
        throw new RuntimeException("y is beyond the board's BOTTOM");
      }
      y = newY;
    }
  } 
