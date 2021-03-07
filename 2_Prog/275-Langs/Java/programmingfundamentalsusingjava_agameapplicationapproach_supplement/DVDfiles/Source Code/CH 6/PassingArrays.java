  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class PassingArrays extends DrawableAdapter
  { static PassingArrays ge = new PassingArrays(); 
    static GameBoard gb = new GameBoard(ge, "Passing Arrays to Methods");
    static SnowmanV7[] parade = new SnowmanV7[8]; 

    public static void main(String[] args) 
    { 
      int[] ages = new int[5];
 
      for(int i = 0; i < 5; i++)
      { 
        ages[i] = 21 + i;
     } 
      birthday(ages);
      for(int i = 0; i < 5; i++)
      {      System.out.print(ages[i] + " ");
      } 

      for(int i = 0; i < 8; i++)
      {
        parade[i] = new SnowmanV7(10 + i * 50, 100 + i * 30);
      }

      gb.setTimerInterval(3, 20);
      showGameBoard(gb);
    }

    public void draw(Graphics g)
    { 
      for(int i = 0; i < 8; i++)
      {
        parade[i].show(g); // show the parade at its current location
      }		
    }

    public void timer3()
    {	    
      move(parade);
      bounce(parade);
   }
 
    static  void birthday(int[] theAges)
    {    
      for(int i = 0; i < theAges.length; i++)
      {
       theAges[i] = theAges[i] + 1;
      }
    }

    static void move(SnowmanV7[] sm)
    { 
      int x, y;

      for(int i = 0; i < 8;  i++)
      {	
        x = sm[i].getX();
        x = x + sm[i].getXSpeed();
        sm[i].setX(x);
        y = sm[i].getY();
        y = y + sm[i].getYSpeed();
        sm[i].setY(y);
      }
    }

    static void bounce(SnowmanV7[] sm)
    { 
      int speed;

      for(int i = 0; i < 8; i++)
      {	
        if(sm[i].getX() >= 460 || sm[i].getX() <= 6)
        {	
          speed = sm[i].getXSpeed();
          speed = -speed;
          sm[i].setXSpeed(speed);
        }	
        if(sm[i].getY() >= 420 || sm[i].getY() <= 30)
        {	
          speed = sm[i].getYSpeed();
          speed = -speed;
          sm[i].setYSpeed(speed);
       }	
      }
    }
  }
