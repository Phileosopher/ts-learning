   import edu.sjcny.gpv1.*;
   import java.awt.*;

   public class OverloadingConstructors extends DrawableAdapter
   { 
     static OverloadingConstructors ga= new OverloadingConstructors( ); 
     static GameBoard gb = new GameBoard(ga, "Overloading Constructors");
     static SnowmanV6 sm1 = new SnowmanV6( 7, 30);
     static SnowmanV6 sm2 = new SnowmanV6 (250, 250);
     static SnowmanV6 sm3 = new SnowmanV6(350, 250, Color.BLUE);
 	
     public static void main(String[] args) 
     { 	
       showGameBoard(gb);
     }

     public void draw(Graphics g) //the drawing call back method
     { 	
       sm1.show(g); 
       sm2.show(g);
       sm3.show(g);
     }
   }
