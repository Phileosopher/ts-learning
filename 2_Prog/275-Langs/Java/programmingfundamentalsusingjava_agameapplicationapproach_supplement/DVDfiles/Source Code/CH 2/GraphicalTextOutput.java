       import edu.sjcny.gpv1.*;
       import java.awt.Graphics;
    
       public class GraphicalTextOutput extends DrawableAdapter
       { 
         static GraphicalTextOutput ga = new GraphicalTextOutput( ); 
         static GameBoard gb = new GameBoard(ga, "Graphical Text Output");
    	
         public static void main(String[] args) 
        {	
          showGameBoard(gb);
        }
    
        public void draw(Graphics g) //the drawing call back method
        {	
          g.drawString("Hello World", 250, 220);
    	
        }
      }
