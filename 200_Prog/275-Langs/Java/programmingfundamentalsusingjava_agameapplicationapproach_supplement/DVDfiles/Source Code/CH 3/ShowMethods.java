       import edu.sjcny.gpv1.*;
       import java.awt.Graphics;
       public class ShowMethods extends DrawableAdapter
       { 
         static ShowMethods ga = new ShowMethods( ); 
         static GameBoard gb = new GameBoard(ga, "Show Methods");
         static SnowmanV2 sm1 = new SnowmanV2();
    	
         public static void main(String[] args) 
        {	
          System.out.println(sm1);
          sm1.showXYToSC();
    
          showGameBoard(gb);
        }
    
        public void draw(Graphics g) //the drawing call back method
        {	
    	sm1.show(g); 
    
        }
      }
