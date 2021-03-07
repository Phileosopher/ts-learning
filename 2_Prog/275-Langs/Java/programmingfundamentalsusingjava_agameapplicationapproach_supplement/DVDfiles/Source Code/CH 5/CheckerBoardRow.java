     import java.awt.*;
     import edu.sjcny.gpv1.*;
    
     public class CheckerBoardRow extends DrawableAdapter
     {
        static CheckerBoardRow ge = new CheckerBoardRow (); 
        static GameBoard gb = new GameBoard(ge, "Checker Board Row");

        public static void main(String[] args) 
        {   
          showGameBoard(gb);
        }
    
        public void draw(Graphics g)
        { 
          int boxX = 12;
          int boxY = 50;
          int boxWidth = 60;
          int boxHeight = 53;
          int checkerX = 20;
          int checkerY = 55;
          int firstCheckerCol = 1;
          Color firstColor = Color.BLACK;
          Color secondColor = Color.RED;
    
          gb.setBackground(Color.LIGHT_GRAY);
    
          //Draw the Checker board boxes
          for(int col = 1; col <= 8; col++)
          {
            g. setColor(firstColor); //black
            if(col % 2 == 0)
            { 	
              g. setColor(secondColor); //red
            } //end if
            g.fillRect(boxX, boxY, boxWidth, boxHeight);
            boxX = boxX + boxWidth;
          } //end for loop
    
          //Draw the Red checkers
          g.setColor(Color.RED);
          for(int col = firstCheckerCol; col <=8; col= col + 2)
          {	
            checkerX = 20 + (col - 1) * boxWidth;
            g.fillOval(checkerX, checkerY, 40, 40);
          }
        }
      }
