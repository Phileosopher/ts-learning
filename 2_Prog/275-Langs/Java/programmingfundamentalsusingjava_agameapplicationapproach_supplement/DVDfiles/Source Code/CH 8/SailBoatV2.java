   import java.awt.*;

   public class SailBoatV2 extends SailBoat //overriding a parent method
   {                                        
     public SailBoatV2(int x, int y, int length, Color color)
     {
       super(x, y, length, color); //invoke the parent's constructor
     }

    @Override //translator verified an inherited method has this signature
    public void show(Graphics g) // overwrites the parent's method
    {
      super.show(g); //invoke the parent's method to draw the boat
      g.setColor(Color.BLACK); //draw the mast
      g.fillRect(getX() + getLength()/2, getY() - getLength()/2,
                 3, getLength()/2); 
    }
  }
