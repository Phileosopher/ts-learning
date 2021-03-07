  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class DeepAndShallow extends DrawableAdapter
  { static DeepAndShallow ge = new DeepAndShallow (); 
    static GameBoard gb = new GameBoard(ge, "Deep and Shallow Data");
    static ParentSnowmanV2[] ps;
    static boolean gameOver = false;
 
    public static void main(String[] args) 
    { ps = new ParentSnowmanV2[10];
      ps[0] = new ParentSnowmanV2(100, 200, "G", Color.BLUE);
      ps[1] = new ParentSnowmanV2(300, 275, "1", Color.GREEN);
      ps[2] = new ParentSnowmanV2(300, 400, "2", Color.GREEN);
      ps[3] = new ParentSnowmanV2(100, 100, "3", Color.GREEN);

      gb.setTimerInterval(3, 20);
      showGameBoard(gb);
    }

    public void draw(Graphics g)
    {
      for(int i = 1; i < ps.length; i++)
      {
        if(ps[i] != null) //the snowman exists
        {
          ps[i].show(g);
        }
      }
      ps[0].show(g); //the patrolling guard
    }

    public void timer3()
    { int x, speed, y;
      if(ParentSnowmanV2.getSnowmanCount()== 10)
      {
        gb.stopTimer(3);
        gameOver = true;
      }
      //move the guard
      x = ps[0].getX();
      x = x + ps[0].getXSpeed();
      ps[0].setX(x);
      y = ps[0].getY();
      y = y + ps[0].getYSpeed();
      ps[0].setY(y);

      //is ps[0] at a border?
      if(ps[0].getX() >= 460 || ps[0].getX() <= 6) 
      {
        speed = ps[0].getXSpeed();
        speed = -speed;
        ps[0].setXSpeed(speed);
        ps[ParentSnowmanV2.getSnowmanCount()] = ps[0].partialClone();
      }	
      if(ps[0].getY() >= 423 || ps[0].getY() <= 30) 
      {
        speed = ps[0].getYSpeed();
        speed = -speed;
        ps[0].setYSpeed(speed);
        ps[ParentSnowmanV2.getSnowmanCount()] = ps[0].partialClone();
      }

      // has ps[0] found a green-hat wandering snowman?
      for(int i = 1; i <= ps.length; i++)
      {
        if(ps[i] != null && ps[0].collidedWith(ps[i]) &&
           !ps[0].equals(ps[i]))
        {
          ps[i].setX(ps[0].getX()); //position the wanderer behind ps[0]
          ps[i].setY(ps[0].getY());
        }
      }
    }

    public void leftButton()
    {
      if(gameOver == true)
      { for(int i=0; i<=3; i++) //move the three intruders left
        {
          ps[i].setX(ps[i].getX() - (i * 3));	
        }
        ps[0].setX(ps[0].getX() - 1); // move the guard	
      }				
    }	
  }
