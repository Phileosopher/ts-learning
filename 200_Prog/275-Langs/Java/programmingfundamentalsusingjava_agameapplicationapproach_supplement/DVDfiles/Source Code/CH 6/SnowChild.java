    import java.awt.*;

    public class SnowChild 
    {
      private int x = 8;
      private int y = 30;
      private boolean visible = true;
      private String name;

    public SnowChild()  
    {   
    }

    public SnowChild(int intialX, int intialY, String name)  
    { x = intialX;  
      y = intialY;
      this.name = name;
      }

    public void show(Graphics g) //g is the game board object
    { int[] xPoly = {x + 15, x + 12, x + 18};
      int[] yPoly = {y + 5, y + 8, y + 8};

      g.setColor(Color.WHITE);
      g.fillOval(x + 8, y, 14, 14); //head
      g.fillOval(x, y + 14, 28, 28); //body
      g.setColor(Color.RED);
      g.fillPolygon(xPoly, yPoly, 3); //nose
      g.setColor(Color.BLACK);		
      g.setFont(new Font("Arial", Font.BOLD, 16));
      g.drawString(name, x + 10, y + 33);  //name
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

    public void setName(String newName)
    { name = newName;
    }

    public String getName()
    { return name;
    }
  }
