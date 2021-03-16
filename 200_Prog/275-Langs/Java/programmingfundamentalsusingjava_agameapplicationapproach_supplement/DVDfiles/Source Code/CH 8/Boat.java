  import java.awt.*;
  import java.io.Serializable;

  public abstract class Boat implements Serializable //contains items 
  {                                                  //common to all boats
    private static int PRICE_PER_FOOT = 10;
    private int x, y, length; //data members common to all types of boats
    private Color color;
   
    public Boat(int x, int y, int length, Color color)
    {
      this.x = x;
      this.y = y;
      this.length = length;
      this.color = color;
    }
    public int calculatePrice() //will be overridden
    {
      return length * PRICE_PER_FOOT; 
    }
    public void show(Graphics g) //will be overridden
    {
      int[] xBoat = {getX() , getX() + length, getX() + 6*length/7,
                     getX() + length/14};
      int[] yBoat = {getY(), getY(), getY() + length/7,
                     getY() + length/7};
      int price = calculatePrice();
      g.setColor(color);
      g.fillPolygon(xBoat, yBoat, xBoat.length);
      g.setColor(Color.BLACK);		
      g.setFont(new Font("Arial", Font.BOLD, 16));
      g.drawString("$" + String.valueOf(price), x + 10, y + 16); 
    }
    public String toString() //will be overridden
    {
      return "Location: (" + x + ", " + y +"), length: " + length +
                         ",Color: " + color;
    }
    public int getX() //get & set methods common to all types of boats
    {
      return x;
    }
    public int getY()
    {
      return y;
    }
    public int getLength()
    {
      return length;
    }
    public Color getColor()
    {
      return color;
    }
    public void setX(int x)
    {
      this.x = x;
    }
    public void setY(int y)
    {
      this.y = y;
    }
  }
