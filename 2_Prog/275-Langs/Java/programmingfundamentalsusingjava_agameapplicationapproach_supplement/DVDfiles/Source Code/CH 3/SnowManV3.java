   import java.awt.Color;
   import java.awt.Graphics; //needed for drawing shapes

   public class SnowmanV3  
   {   
     //data members  
     public int x = 5;
     public int y = 30;
     public Color hatColor = Color.BLACK;
 
     // member methods
     public SnowmanV3(int x, int y)
     {
       this.x = x;
       this.y = y;
     }

     public void showXYToSC()
     {
       System.out.println("x is: " + x +
                          "\ny is: " + y);
     }

     public void show(Graphics g) // g is passed to the method
     {
       g.setColor(hatColor);
       g.fillRect(x + 15, y, 10, 15); //hat
       g.fillRect(x + 10, y + 15, 20, 2); //brim
       g.setColor(Color.WHITE);
       g.fillOval(x + 10, y + 17, 20, 20); //head 
       g.fillOval(x, y + 37, 40, 40); //body
     }
   }
