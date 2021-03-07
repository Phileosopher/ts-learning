   import edu.sjcny.gpv1.*;
   import javax.swing.*;
   import java.awt.*;

   public class ObjectsAsParameters extends DrawableAdapter
   { 
     static ObjectsAsParameters ga = new ObjectsAsParameters(); 
     static GameBoard gb = new GameBoard(ga, "Objects As Parameters");
     static SnowmanV6 sm1 = new SnowmanV6(5, 40, Color.RED);  
     static SnowmanV6 sm2 = new SnowmanV6(460, 423, Color.BLUE); 
	
     public static void main(String[] args) 
     { 
       String s = JOptionPane.showInputDialog("sm2's new x location?");
       int newX = Integer.parseInt(s);
       sm2.setX(newX);	
       showGameBoard(gb);
     }

     public void draw(Graphics g) // the drawing call back method
     {	
       sm1.show(g); 
       sm2.show(g);
     }

     public void rightButton() //moves sm1 & sm2 one pixel right per click
     {
       moveRight(sm1);
       moveRight(sm2);     
     }

     public static void moveRight(SnowmanV6 aSnowman) 
     {
       int currentX = aSnowman.getX( );
       currentX++;
       aSnowman.setX(currentX);
     }
   }
