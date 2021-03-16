   import java.awt.*;
   import javax.swing.*; // needed for drawing shapes

   public class SnowmanV5 
   {   
     //data members
     private int x = 7;
     private int y = 30;
     private Color hatColor = Color.BLACK;

     //member methods
     public SnowmanV5(int x, int y)  
     {    
       this.x = x;  
       this.y = y;
     }

     public void show(Graphics g) //g is passed to the method
     {
       g.setColor(hatColor);
       g.fillRect(x + 15, y, 10, 15); //hat 
       g.fillRect(x + 10, y + 15, 20, 2); //brim
       g.setColor(Color.WHITE);
       g.fillOval(x + 10, y + 17, 20, 20); //head
       g.fillOval(x, y + 37, 40, 40); //body

     }

     public String toString()
     {
       String s;
       s = "x is: " + x +
           "\ny is: " + y +
           "\nhatColor is: " + hatColor;
       return s;
     }

     public void input()
     {
       String s;
       int red, green, blue;

       s = JOptionPane.showInputDialog("enter the value of x");
       x = Integer.parseInt(s);
       s = JOptionPane.showInputDialog("enter the value of y");
       y = Integer.parseInt(s);
       s = JOptionPane.showInputDialog("enter hat's red intensity");
       red = Integer.parseInt(s);
       s =JOptionPane.showInputDialog("enter hat's green intensity");
       green = Integer.parseInt(s);
       s = JOptionPane.showInputDialog("enter hat's blue intensity");
       blue = Integer.parseInt(s);
       hatColor = new Color(red, green, blue);
     }
   }
