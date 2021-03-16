    import edu.sjcny.gpv1.*; 
    import java.awt.*;

    public class LinesAndShapes extends DrawableAdapter
    { 
      static LinesAndShapes ga = new LinesAndShapes(); 
      static GameBoard gb = new GameBoard(ga, "Lines and Shapes");
 	
      public static void main(String[] args) 
      {	
        showGameBoard(gb);
      }

      public void draw(Graphics g) // the drawing call back method
      {	
        g.drawLine(100, 75, 260, 75);	//Lines
        g.drawLine(300, 50, 400, 100);
    	
        g.setColor(Color.DARK_GRAY);	
        g.drawRect(100, 170, 100, 60);  	//Rectangles
        g.fillRect(280, 170, 150, 40);  
		
        g.setColor(Color.RED);
        g.drawOval(55, 300, 180, 80);  	//Ovals
        g.setColor(Color.BLUE);
        g.fillOval(280, 300, 100, 100);  

      }
    }
