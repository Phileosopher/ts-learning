   import java.awt.*;
   import javax.swing.*; 

   public class BoxedSnowman 
   {
     private int x = 8;
     private int y = 30;
     private Color hatColor = Color.BLACK;
     private boolean visible = true;

     public BoxedSnowman(int intialX, int intialY, Color hatColor)  
     { x = intialX;  
       y = intialY;
       this.hatColor = hatColor;
     }

     public void show(Graphics g) //g is the game board object
     {   
       g.setColor(Color.hatColor);
       g.fillRect(x + 15, y, 10, 15); //hat
       g.fillRect(x + 10, y + 15, 20, 2); //brim
       g.setColor(Color.WHITE);
       g.fillOval(x + 10, y + 17, 20, 20); // head
       g.fillOval(x, y + 37, 40, 40); //body
       g.setColor(Color.RED);
       g.fillOval(x + 19, y + 53, 4, 4); //button
       g.setColor(Color.BLACK);
       g.drawRect(x, y, 40, 77); //inscribing rectangle
     }

     public int getX()
     {
       return x;
     }

     public void setX(int newX)
     {
       x = newX;
     }
     public int getY()
     {
       return y;
     }

     public void setY(int newY)
     {
       y = newY;
     }

     public boolean getVisible()
     {
       return visible;
     }

     public void setVisible(boolean newVisible)
     {
       visible = newVisible;
     }
   } 
