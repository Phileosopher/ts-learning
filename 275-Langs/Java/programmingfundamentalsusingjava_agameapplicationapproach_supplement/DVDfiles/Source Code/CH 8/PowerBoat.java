  import java.awt.*;

  public class PowerBoat extends Boat 
  {                                          
    private int horsePower; //extended (additional) data member

    public PowerBoat(int x, int y, int length, 
                     Color color, int horsePower)
    {
      super(x, y, length, color);
      this.horsePower = horsePower;
    }
    @Override
    public int calculatePrice() //overrides parent method
    {
      int hullPrice = super.calculatePrice();
      return hullPrice + horsePower * 3; 
    }
    @Override
    public void show(Graphics g) //overrides parent method
    {
      int[] xSail = {getX() + getLength()/2, getX(),
                     getX() + getLength()/2,};
      int[] ySail = {getY() - getLength()/2, getY() - getLength()/8,
                     getY() - getLength()/8};

      super.show(g);
      g.setColor(Color.BLACK); //draw the shaft
      g.fillOval(getX() - 13, getY() + getLength()/7 , 30, 4); 		
      g.setColor(Color.GRAY); //draw the propeller
      g.fillOval(getX() - 20, getY() + getLength()/7, 20, 6); 		
      g.fillOval(getX() - 13, getY() + getLength()/7 - 7, 6, 20); 		
    }
    public String toString()//overrides parent method
    {
      return super.toString() + ", Horsepower: " + horsePower;
    }	
  }
