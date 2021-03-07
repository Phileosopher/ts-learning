  import java.awt.*;

  public class SnowmanV8 
  {
    private static int w = 40;
    private static int h = 77;
    private int x;
    private int y;
    private String name; //data members for aggregated objects
    private Hat aHat;

    public SnowmanV8(int intialX, int intialY) 
    {
      x = intialX;  
      y = intialY;
      name = "sm"; //aggregates a String object into this class			
    }
    public void show(Graphics g) 
    { int[] xPoly = {x + 20, x + 15, x + 25};
      int[] yPoly = {y + 8, y + 13, y + 13};

      if(aHat != null) //snowman has a hat
      {	
        aHat.setX(x + w/2 - aHat.getW()/2); //locate the hat on the head
       aHat.setY(y - aHat.getH());
        aHat.show(g); //draw the hat
      }
      g.setColor(Color.WHITE);
      g.fillOval(x + 10, y, 20, 20); // head
      g.fillOval(x, y + 20, 40, 40); // body
      g.setColor(Color.RED);
      g.fillPolygon(xPoly, yPoly, 3); // nose 
      g.setColor(Color.BLACK);		
      g.setFont(new Font("Arial", Font.BOLD, 16));
      g.drawString(name, x + 10, y + 45); // name
    }

    public boolean collidedWith(Hat hat)
    {
      if( !(x > hat.getX( ) + hat.getW() || x + w < hat.getX( ) ||
            y > hat.getY( ) + hat.getH() || y + h < hat.getY( )))
      {
        return true;
      }
      else
      {
        return false;
      }
    }
    public void setHat(Hat newHat)
    {
      aHat = newHat; //aggregates a Hat object into this class
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
