  import java.awt.*;
  
  public class SailBoatV3 extends SailBoatV2
  {
    private static int pricePerSquareFoot = 2;
    private int sailArea; // additional data members

    public SailBoatV3(int x, int y, int length, 
                      Color color, int sailArea)
    {
      super(x, y, length, color);
      this.sailArea = sailArea;
    }

    @Override
    public int calculatePrice() //invokes the method it overrides
    {
      int hullPrice = super.calculatePrice(); //invokes RowBoat's method
      return hullPrice + sailArea * pricePerSquareFoot;
    }

    @Override
    public void show(Graphics g) 
    {
      int[] xSail = {getX() + getLength()/2, getX(),
                     getX() + getLength()/2,};
      int[] ySail = {getY() - getLength()/2, getY() - getLength()/8,
                     getY() - getLength()/8};

      g.setColor(Color.WHITE); //draw the sail
      g.fillPolygon(xSail, ySail, xSail.length); 
      super.show(g);
    }
  }
