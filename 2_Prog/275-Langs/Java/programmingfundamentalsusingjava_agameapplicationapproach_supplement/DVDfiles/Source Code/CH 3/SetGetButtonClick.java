   import edu.sjcny.gpv1.*;
   import javax.swing.*;
   import java.awt.Graphics;

   public class SetGetButtonClick extends DrawableAdapter
   { 
     static SetGetButtonClick ga = new SetGetButtonClick(); 
     static GameBoard gb = new GameBoard(ga,"Get Set and Button Click");
     static SnowmanV4 sm1 = new SnowmanV4(5, 40); //top-left corner 
    static SnowmanV4 sm2 = new SnowmanV4(460, 423); //bottom-right corner

    public static void main(String[] args) 
    { 
      String s = JOptionPane.showInputDialog("sm2's new x location?");
      int newX = Integer.parseInt(s);
      sm2.setX(newX);	
      showGameBoard(gb);
    }

    public void draw(Graphics g) //the drawing call back method
    {
      sm1.show(g); 
      sm2.show(g);
    }

    public void rightButton() //moves sm1 one pixel right per click
    {
      int currentX = sm1.getX( );
      sm1.setX(currentX + 1);
    }
  }
