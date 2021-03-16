  import java.awt.*;

  public class ParentSnowmanV2
  {
    private static int snowmanCount = 0;
    private static int w = 40;
    private static int h = 77;
    private int x = 8;
    private int y = 30;
    private String name;
    private Color hatColor= Color.BLACK;
    private int xSpeed = 2;
    private int ySpeed = 2;
    private boolean visible = true;
         
    public ParentSnowmanV2()  
    {  
      snowmanCount++;
    }
    public ParentSnowmanV2(int intialX, int intialY, String name, 
                           Color hatColor) 
    {
      x = intialX;  
      y = intialY;
      this.name = name;
      this.hatColor = hatColor;
      snowmanCount++;
    }
    private void copy(ParentSnowmanV2 ps) //copies 4 data members
    {
      ps.setX(x); 
      ps.setY(y);   
      ps.setName(name);
      ps.setHatColor(hatColor);  
    }
    public ParentSnowmanV2 partialClone() 
    {
      ParentSnowmanV2 theClone = new ParentSnowmanV2(); 
      this.copy(theClone);  
      return theClone; 
    }
    public boolean shallowEquals(ParentSnowmanV2 ps)
    {
      if(this == ps)
      {  
        return true;
      }
      else
      {
        return false;
      }
    }
    public boolean equals(ParentSnowmanV2 ps)
    {
      if(hatColor.equals(ps.getHatColor())) //same hat color
      {  
        return true; 
      }
      else
      {
        return false; 
      }     
    }
    public boolean collidedWith(ParentSnowmanV2 ps)
    {
      if( !(x > ps.getX( ) + w || x + w < ps.getX( ) ||
            y > ps.getY( ) + h || y + h < ps.getY( )))
      {
       return true;
      }
      else
      {
       return false;
      } 
    }  
    public void show(Graphics g) // g is the game board object
    { 
      int[] xPoly = {x + 20, x + 15, x + 25};
      int[] yPoly = {y + 25, y + 30, y + 30};
 
      g.setColor(hatColor);
      g.fillRect(x + 15, y, 10, 15);  // hat
      g.fillRect(x + 10, y + 15, 20, 2);  // brim
      g.setColor(Color.WHITE);
      g.fillOval(x + 10, y + 17, 20, 20); // head
      g.fillOval(x, y + 37, 40, 40);  // body
      g.setColor(Color.RED);
      g.fillPolygon(xPoly, yPoly, 3); // nose 
      g.setColor(Color.BLACK);  
      g.setFont(new Font("Arial", Font.BOLD, 16));
      g.drawString(name, x + 16, y + 62); // name
    }
    public static int getSnowmanCount()
    { 
      return snowmanCount; 
    }
    public int getXSpeed()
    { 
      return xSpeed; 
    }
    public void setXSpeed(int newXSpeed)
    { 
      xSpeed = newXSpeed;
    }
    public int getYSpeed()
    { 
      return ySpeed; 
    }
    public void setYSpeed(int newYSpeed)
    { 
      ySpeed = newYSpeed;
    }
    public void setHatColor(Color newHatColor)
    {  
      hatColor = newHatColor;
    } 
    public Color getHatColor()
    { 
      return hatColor; 
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
    public String getName()
    { 
      return name;
    }
    public void setName(String newName)
    {
      name = newName;
    }
    public boolean getVisible()
    {
      return visible;
    }
  }
