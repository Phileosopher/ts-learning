import edu.sjcny.gpv1.*;
import java.awt.Graphics;

public class ConstructorAndThis extends DrawableAdapter
{ 
   static ConstructorAndThis ga = new ConstructorAndThis(); 
   static GameBoard gb = new GameBoard(ga,"Constructors and Key	Word: this");
   static SnowmanV3 sm1 = new SnowmanV3(5, 30);
   static SnowmanV3 sm2 = new SnowmanV3(460, 423);
		
   public static void main(String[] args) 
   {	
     showGameBoard(gb);
   }

   public void draw(Graphics g) //the drawing call back method
   {	
     sm1.show(g); 
     sm2.show(g);

   }
}
