  import java.awt.Graphics;
  import edu.sjcny.gpv1.*;
   
  public class SnowmanParade  extends DrawableAdapter
  { static SnowmanParade ge = new SnowmanParade(); 
    static GameBoard gb = new GameBoard(ge, "Snowman Parade");
    static SnowmanV7[] parade = new SnowmanV7[8]; 
 
    public static void main(String[] args) 
    {
      for(int i=0; i < parade.length; i++) //create each snowman
      {
        parade[i] = new SnowmanV7(10 + i * 50 , 100 + i * 30);
      }	
      gb.setTimerInterval(3, 20);
      showGameBoard(gb);
    }

    public void draw(Graphics g) //draw each snowman
    {
      for(int i = 0; i < parade.length; i++) 
      {
        parade[i].show(g); 
      }		
    }

    public void timer3()
    {
      int x, speed, y;

      for(int i = 0; i  <parade.length; i++) //move each snowman
      {	
        x = parade[i].getX();
        x = x + parade[i].getXSpeed();
        parade[i].setX(x);
        y = parade[i].getY();
        y = y + parade[i].getYSpeed();
        parade[i].setY(y);
     }

      for(int i = 0; i < parade.length; i++) //reflect each snowman
      {	
        if(parade[i].getX() >= 460 || parade[i].getX() <= 6) //x reflection
        {	
          speed = parade[i].getXSpeed();
          speed = -speed;
          parade[i].setXSpeed(speed);
        }	
        if(parade[i].getY() >= 420 || parade[i].getY() <= 30)//y reflection
        {	
          speed = parade[i].getYSpeed();
          speed = -speed;
          parade[i].setYSpeed(speed);
        }	
      }
    }
  }
