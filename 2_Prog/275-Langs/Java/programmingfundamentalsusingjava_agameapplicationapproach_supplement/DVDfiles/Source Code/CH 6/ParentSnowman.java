    import java.awt.*;

    public class ParentSnowman 
    {
      private int x = 8;
      private int y = 30;
      private boolean visible = true;
      private String name;

    public ParentSnowman()  
    {   
    }

    public ParentSnowman(int intialX, int intialY, String name) 
    { x = intialX;  
      y = intialY;
      this.name = name;
    }

    public void show(Graphics g) // g is the game board object
    { int[] xPoly = {x + 20, x + 15, x + 25};
      int[] yPoly = {y + 25, y + 30, y + 30};

      g.setColor(Color.BLACK);
      g.fillRect(x + 15, y, 10, 15); //hat
      g.fillRect(x + 10, y + 15, 20, 2); //brim
      g.setColor(Color.WHITE);
      g.fillOval(x + 10, y + 17, 20, 20); //head
      g.fillOval(x, y + 37, 40, 40);  //body
      g.setColor(Color.RED);
      g.fillPolygon(xPoly, yPoly, 3); //nose 
      g.setColor(Color.BLACK);		
      g.setFont(new Font("Arial", Font.BOLD, 16));
      g.drawString(name, x + 16, y + 62); //name
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

    public boolean getVisible()
    { return visible;
    }

    public void setVisible (boolean newVisible)
    { visible  = newVisible;
    }

    public String getName()
    { return name;
    }

  }
