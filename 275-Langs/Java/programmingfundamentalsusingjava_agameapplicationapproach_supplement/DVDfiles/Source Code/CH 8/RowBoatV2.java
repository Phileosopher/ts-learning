  import java.awt.*;

  public class RowBoatV2 extends Boat
  {
    private int oars; //extended (additional) data member
    
    public RowBoatV2(int x, int y, int length, Color c, int oars)
    {
      super(x, y, length, c);
      this.oars = oars;
    }
    @Override
    public int calculatePrice() //overrides parent method
    {
      int hullPrice = super.calculatePrice();
      return hullPrice + oars * 10; 
    }
    @Override
    public void show(Graphics g) //overrides parent method
    {
      super.show(g);
      g.setColor(Color.BLACK);
      for(int i = 1; i <= oars; i++) //each ore
      {
        g.fillRect(getX() + i*10, getY() - 20, 2, 20); //handle
        g.fillOval(getX() + i*10-2, getY() - 30, 6, 10); //paddle
      }
    }
    public String toString() //overrides parent method
    {
      return super.toString() + ", Oars: " + oars;
    }
  }
