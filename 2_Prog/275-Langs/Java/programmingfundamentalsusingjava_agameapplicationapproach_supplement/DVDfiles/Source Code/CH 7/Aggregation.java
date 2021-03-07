  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class Aggregation extends DrawableAdapter
  { static Aggregation ge = new Aggregation(); 
    static GameBoard gb = new GameBoard(ge, "Aggregation");
    static Hat[] hats = new Hat[6];
    static SnowmanV8 sm;

    public static void main(String[] args) 
    {   
      hats[0] = new Hat(40, 100, Color.RED, 20, 17);
      hats[1] = new Hat(120, 100, Color.ORANGE, 25, 21);
      hats[2] = new Hat(200, 100, Color.YELLOW, 20, 17);
      hats[3] = new Hat(280, 100, Color.GREEN, 40, 34);
      hats[4] = new Hat(360, 100, Color.BLUE, 30, 25);
      hats[5] = new Hat(440, 100, Color.MAGENTA, 35, 29);
      sm = new SnowmanV8(250, 250); 

      showGameBoard(gb);
    }

    public void draw(Graphics g)
    {
      g.setColor(Color.BLACK); //the hat rack
      g.fillRect(20, 95, 460, 5);
      for(int i=0; i<hats.length; i++)
      {
        hats[i].show(g);
      }
      sm.show(g);
    }
    public void keyStruck(char key) //call back method
    {
      int newX, newY;

      switch (key) //to move the snowman
      {
        case 'L':
        {
          newX = sm.getX() - 2; 
          sm.setX(newX);
          break;
        }
        case 'R':
        {
          newX = sm.getX() + 2; 
          sm.setX(newX);
          break;
        }
        case 'U':
        {
          newY = sm.getY() - 2;
          sm.setY(newY);
          break;
        }
        case 'D':
        {
          newY = sm.getY() + 2;
          sm.setY(newY);
        }
      } 
      //acquiring a new Hat
      for(int i = 0; i<hats.length; i++)
      {
        if(sm.collidedWith(hats[i])) //a hat is chosen
        {
          sm.setHat(hats[i].clone()); //clone the hat and add it to sm
        }
      }  
    }
  }
