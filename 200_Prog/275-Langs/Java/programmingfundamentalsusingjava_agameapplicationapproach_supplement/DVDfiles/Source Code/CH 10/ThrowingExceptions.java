  import edu.sjcny.gpv1.*;
  import java.awt.*;
  import javax.swing.*;

  public class ThrowingExceptions extends DrawableAdapter
  { static ThrowingExceptions ge = new ThrowingExceptions (); 
    static GameBoard gb = new GameBoard(ge, "THROWING EXCEPTIONS");
    static BoxedSnowman2 s1;
    static String message = "";
    
    public static void main(String[] args) 
    { String s;
      boolean correctXY = false;
      int x, y;
   
      while(correctXY == false) //x or y is not valid
      { s = JOptionPane.showInputDialog("enter the snowman's " +
                                        "X coordinate");
        x = Integer.parseInt(s);
        s = JOptionPane.showInputDialog("enter the snowman's " +
                                        "Y coordinate");
        y = Integer.parseInt(s);

        try
        {
          s1 = new BoxedSnowman2(x, y, Color.BLUE); //exception produced?
          correctXY = true;
        } //end try
        catch(RuntimeException e)
        {
          JOptionPane.showMessageDialog(null, e.getMessage());
        } //end catch
      } //end while 
 
      showGameBoard(gb);
    }

    public void draw(Graphics g)
    {
      g.setColor(Color.BLACK);
      g.setFont(new Font("Arial", Font.BOLD, 18));
      g.drawString(message,  120, 50);
      s1.show(g);
    }	

    public void keyStruck(char key)
    { int newX, newY;
      message = "";
     
      try
      {
        switch (key)
        {
          case 'L':
          {	
            newX = s1.getX() - 2; 
            s1.setX(newX); //could cause an exception
            break;
          }
          case 'R':
          {	
            newX = s1.getX() + 2; 
            s1.setX(newX); //could cause an exception
            break;
          }
          case 'U':
          {
            newY = s1.getY() - 2;
            s1.setY(newY); //could cause an exception
            break;
          }
          case 'D':
          {
            newY = s1.getY() + 2;
            s1.setY(newY); //could cause an exception
          }
        }
      } // end try 
      catch(RuntimeException e)
      {
        message = e.getMessage();
      } //end catch	
    }
  }
