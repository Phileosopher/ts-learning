  import java.awt.*;
  public class RowBoat 
  {
    private static int PRICE_PER_FOOT = 10;
    private int x, y, length;
    private Color color = Color.GREEN;

    public RowBoat()
    {

    }
    public RowBoat(int x, int y, int length)
    {
      this.x = x;
      this.y = y;
      this.length = length;
    }
    public int calculatePrice()
    {
      return length * PRICE_PER_FOOT; 
    }
    public void show(Graphics g)
    {
      int[] xBoat = {x , x + length, x + 6 * length / 7,  x + length/14};
      int[] yBoat = {y,  y,          y + length / 7, y + length / 7};
      int price = calculatePrice();
      g.setColor(color); //draw the Boat
      g.fillPolygon(xBoat, yBoat, xBoat.length);
      g.setColor(Color.BLACK); //draw the boat's price in black		
      g.setFont(new Font("Arial", Font.BOLD, 16));
      g.drawString("$" + String.valueOf(price), x + 10, y + 16); 
    }
    public int getX()
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
    public void setLength(int length)
    {
      this.length = length;
    }
      public void setColor(Color color)
    {
      this.color = color;
    }
  }
