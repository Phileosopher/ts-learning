       import edu.sjcny.gpv1.*;
       import java.awt.Graphics;
       import java.awt.Font;
       public class CountingSeconds extends DrawableAdapter
       { 
         static CountingSeconds ga = new CountingSeconds( ); 
         static GameBoard gb = new GameBoard(ga, "The Counting Algorithm");
         static int count = 0;	// a class level variable
    	
         public static void main(String[] args) 
         {	
           showGameBoard(gb);
         }
    
         public void draw(Graphics g) // the drawing call back method
         {	
           g.setFont(new Font("Arial", Font.BOLD, 18));
           g.drawString("Your game time is: " + count, 10, 50);
         }
    
         public void timer1()
         {
           count = count + 1;
         }
       }
