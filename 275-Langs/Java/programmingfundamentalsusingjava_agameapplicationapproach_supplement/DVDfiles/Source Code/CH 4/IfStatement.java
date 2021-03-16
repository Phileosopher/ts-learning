   import edu.sjcny.gpv1.*;
   import java.awt.*;

   public class IfStatement extends DrawableAdapter
   { 
     static IfStatement ga = new IfStatement ( ); 
     static GameBoard gb = new GameBoard(ga, "The if Statement");
     static int count = 0;
     static BoxedSnowman s1 = new BoxedSnowman(250, 215, Color.BLACK);
     
     public static void main(String[] args) 
     {
      showGameBoard(gb);
     }

     public void draw(Graphics g) // the draw call back method
     {	
       g.setFont(new Font("Arial", Font.BOLD, 18));
       g.drawString("Your game time is: " + count, 10, 50);
       if(s1.getVisible() == true && count >= 5)
       {
          s1.show(g);
       }

       if(count == 10)
       {      
          g.drawString("Game Over", 10, 70);
          g.drawString("Have a Good Day", 10, 90);    
       }
     }

     public void timer1()
     {
        count = count + 1;
        if(count == 10)
        { 
           gb.stopTimer(1);
           s1.setVisible(false);
        }
     }
   }
