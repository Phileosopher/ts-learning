   import java.awt.*;

   public class SnowmanV4 
   {   
     //data members
     private int x = 7;
     private int y = 30;
     private Color hatColor = Color.BLACK;

    // member methods
    public SnowmanV4(int x, int y)  
    {    
      this.x = x;  
      this.y = y;
    }
  
    public void show(Graphics g) // g, is passed to the method
    {
      g.setColor(hatColor);
      g.fillRect(x + 15, y, 10, 15); //hat
      g.fillRect(x + 10, y + 15, 20, 2); //brim
      g.setColor(Color.WHITE);
      g.fillOval(x + 10, y + 17, 20, 20); //head
      g.fillOval(x, y + 37, 40, 40); //body
    }
  
    public int getX()
    {
      return x;
    }
  
    public void setX(int newX)
    { 
      x = newX;
    }
  
    public int getY()
    {  
      return y;
    }
  
      public void setY(int newY)
    {	 
      y = newY;
    }
  }
