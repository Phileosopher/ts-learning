   import edu.sjcny.gpv1.*;
   import java.awt.*;
   import javax.swing.*; 

   public class CheckerBoard extends DrawableAdapter
   { 
     static CheckerBoard ge = new CheckerBoard (); 
     static GameBoard gb = new GameBoard(ge, "Nested For loops");

    public static void main(String[] args) 
    {   
      showGameBoard(gb);
    }

    public void draw(Graphics g)
    { 
      int xBox = 12;
      int yBox = 50;
      int boxWidth = 60;
      int boxHeight = 53;
      int firstCheckerCol = 1;
      int checkerX = 20;
      int checkerY = 55;
      Color firstColor = Color.BLACK;
      Color secondColor = Color.RED;
      Color temp;

      gb.setBackground(Color.LIGHT_GRAY);

      //Draw the checker board boxes
      for(int row = 1; row <= 8; row++) //each row
      {	
         for(int col = 1; col <=8; col++) //each column
         {  
           g. setColor(firstColor);
           if(col % 2 == 0)
           { 	
             g. setColor(secondColor);
           }
           g.fillRect(xBox, yBox, boxWidth, boxHeight);
           xBox = xBox + boxWidth;
         } 
         yBox = yBox + boxHeight;
         xBox = 12;
 
         temp = firstColor; //swap the box colors
         firstColor = secondColor;
         secondColor = temp;
      }

      //Draw the red checkers
      for(int row = 1; row <= 3; row++) //first three rows
      {
        if(row % 2 == 0) //an even numbered row
        {
          checkerX = checkerX + boxWidth;
          firstCheckerCol = 2;
        }
        g.setColor(Color.RED);
        for(int col = firstCheckerCol; col <=8; col= col + 2) 
        { //red checker locations
          checkerX = 20 + (col -1) * boxWidth;
          g.fillOval( checkerX, checkerY, 40, 40);
        }
        checkerY = checkerY + boxHeight;
        checkerX = 20;
        firstCheckerCol = 1;
      }
    }    
 } 
