   import java.awt.*;

   public class SailBoat extends RowBoat
   {
     public SailBoat(int x, int y, int length, Color color)
     {
       super(x, y, length); //invoke parent constructor
       setColor(color);  //access parent's protected data method 
     }
   }
