       import java.awt.Color;
       import javax.swing.Graphics; //needed for drawing shapes
    
       public class SnowmanV2  
       {   
         //data members
         public int x = 5;
         public int y = 30;
         public Color hatColor = Color.BLACK;
    
        //member methods
        public void showXYToSC()
        {
          System.out.println("x is: " + x +
                             "\ny is: " + y);
        }
    
        public void show(Graphics g) //g is passed to the method
        {
          g.setColor(hatColor);
          g.fillRect(x + 15, y, 10, 15);  	//hat
          g.fillRect(x + 10, y + 15, 20, 2); 	//brim
          g.setColor(Color.WHITE);
          g.fillOval(x + 10, y + 17, 20, 20); //head
          g.fillOval(x, y + 37, 40, 40);	//body
        }
      }
