  import edu.sjcny.gpv1.*;  
  import java.awt.*;
  import java.util.Scanner; 
  import java.io.*;

  public class ExceptionBasics extends DrawableAdapter
  {  
    static ExceptionBasics ge = new ExceptionBasics (); 
    static GameBoard gb = new GameBoard(ge, "Exception Basics");
    static BoxedSnowman s1 = new BoxedSnowman(300, 200, Color.GREEN);
    static BoxedSnowman s2 = new BoxedSnowman(30, 100, Color.BLACK);
    static int score = 0;
    static int count = 10;

    public static void main(String[] args) 
    {	
      showGameBoard(gb);
    }

    public void draw(Graphics g) // a call back method
    {
      int w = 40;
      int h = 77;
      int s1X, s1Y, s2X, s2Y, temp;

      s1X = s1.getX(); s1Y = s1.getY(); 
      s2X = s2.getX(); s2Y = s2.getY();
      g.setColor(Color.BLACK);
      g.setFont(new Font("Arial", Font.BOLD, 18));
      g.drawString("Time remaining: " + count, 260, 50);

      if(count == 0) // the game is over
      {      
        g.setColor(Color.BLACK);
        g.drawString("Game Over", 205, 70);
        g.drawString("Have a Good Day", 175, 90);

        try
        { 
          int highScore;
          File fileObj = new File("HiScore.txt"); 
          Scanner fileIn = new Scanner(fileObj);
          highScore = fileIn.nextInt();
          fileIn.close();

          if(score >= highScore) // a new high score
          {
            g.drawString("Great, Your Score is the Highest Ever.," +
                         " It Will Be Saved", 10, 110);
            FileWriter fileWriterObj = new FileWriter("HiScore.txt");
            PrintWriter fileOut = new PrintWriter(fileWriterObj, false);

            fileOut.println(score);
            fileOut.close();
          }
          else // not a new high score
          {
            g.drawString("Best Score is: " + highScore + 
                         ", Keep Practicing", 110, 110);
          }
        }
        catch(IOException e)
        { 
          g.drawString("Problems With High Score File", 120, 110);
        }
      }
      else if( !(s2X > s1X + w || s2X + w < s1X || s2Y > s1Y + h ||
                 s2Y + h < s1Y) && s1.getVisible() == true) 
      {
        score = score + 1;
        s1.setVisible(false);
      }
      else if( s2X > s1X + w || s2X + w < s1X || s2Y > s1Y + h ||
               s2Y + h < s1Y) // no collision
      {
        if(s1.getVisible() == false) // not visible
        {  temp = s1.getX();
           s1.setX(s1.getY());
           s1.setY(temp);
           s1.setVisible(true);
        }     
      }

      s2.show(g);
      if(s1.getVisible() == true)
      {
        s1.show(g);
      }
        g.setColor(Color.BLACK);
        g.drawString("Score: " + score, 150, 50);
    }

    public void keyStruck(char key) // a call back method
    {
      int newX, newY;

      switch (key)
      {
        case 'L':
        {	
          newX = s2.getX() - 2; 
          s2.setX(newX);
          break;
        }
        case 'R':
        {	
          newX = s2.getX() + 2; 
          s2.setX(newX);
          break;
        }
        case 'U':
        {
          newY = s2.getY() - 2;
          s2.setY(newY);
          break;
        }
        case 'D':
        {
          newY = s2.getY() + 2;
          s2.setY(newY);
        }
      }
    }
    public void timer1() // a call back method
    {
      count = count - 1;
      if(count == 0)
      { 
        gb.stopTimer(1);
      }
    }
  }
