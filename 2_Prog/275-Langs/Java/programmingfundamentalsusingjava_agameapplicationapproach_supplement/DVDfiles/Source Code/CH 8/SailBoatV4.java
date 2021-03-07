   import java.awt.*;
   
  public class SailBoatV4 extends Boat 
  {                                          
    private int sailArea; //extended (additional) data member

    public SailBoatV4(int x, int y, int length, 
                      Color color, int sailArea)
    {
      super(x, y, length, color);
      this.sailArea = sailArea;
    }
    @Override
    public int calculatePrice() //overrides parent method
    {
      int hullPrice = super.calculatePrice();
      return hullPrice + sailArea * 2; 
    }
    @Override
    public void show(Graphics g) //overrides parent method
    {
      int[] xSail = {getX() + getLength()/2, getX(),
                     getX() + getLength()/2};
      int[] ySail = {getY() - getLength()/2, getY() - getLength()/8,
                     getY() - getLength()/8};

      super.show(g);
      g.setColor(Color.BLACK); //draw the mast
      g.fillRect(getX() + getLength()/2, getY() - getLength()/2, 3, 
                 getLength()/2); 
      g.setColor(Color.WHITE); //draw the sail
      g.fillPolygon(xSail, ySail, xSail.length); 
    }
    public String toString() //overrides parent method
    {
      return super.toString() + ", Sail Area: " + sailArea;
    }
  }
