  import java.awt.*;

  public class SnowmanV7 
  {   
    int x;
    int y;
    int xSpeed = 2;
    int ySpeed = 2;

    public SnowmanV7(int x, int y)  
    { this.x = x;  
      this.y = y;
    }

    public void show(Graphics g) // g is the game board object
    { g.setColor(Color.BLACK);
      g.fillRect(x + 15, y, 10, 15);  // hat
      g.fillRect(x + 10, y + 15, 20, 2);  // brim
      g.setColor(Color.WHITE);
      g.fillOval(x + 10, y + 17, 20, 20); // head
      g.fillOval(x, y + 37, 40, 40);  // body
      g.setColor(Color.RED);
    }

    public int getX()
    { return x;
    }

    public void setX(int newX)
    { x = newX;
    }

    public int getY()
    { return y;
    }

    public void setY(int newY)
    { y = newY;
    }

    public int getXSpeed()
    { return xSpeed;
    }

    public void setXSpeed(int newXSpeed)
    { xSpeed = newXSpeed;
    }

    public int getYSpeed()
    { return ySpeed;
    }

    public void setYSpeed(int newYSpeed)
    { ySpeed = newYSpeed;
    }	    		
  }
