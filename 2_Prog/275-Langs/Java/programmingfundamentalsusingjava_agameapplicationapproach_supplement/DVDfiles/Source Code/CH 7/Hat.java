  import java.awt.*;

  public class Hat 
  {
    private int x;
    private int y;
    private int w = 20;
    private int h = 17;
    private Color hatColor;

    public Hat(int x, int y, Color hatColor, int w, int h)
    {
      this.x = x;
      this.y = y;
      this.hatColor = hatColor;
      this.w = w;
      this.h = h;
    }
    public void show(Graphics g) 
    {
      g.setColor(hatColor);
      g.fillRect(x + w/4, y, w/2, (int)(h*0.9));  // hat top
      g.fillRect(x, y + (int)(h*0.9), w, (int)(h*0.2));  // brim
    }
    public Hat clone() 
    {
         Hat theClone = new Hat(x, y, hatColor, w, h); 
         return theClone; 
    }
    public int getW()
    {
      return w; 
    }
    public int getH()
    {
      return h; 
    }
    public int getX()
    {
      return x; 
    }
    public void setX(int newX)
    {	
      x = newX;
    }
    public int getY()
    {
      return y;
    }
    public void setY(int newY)
    {
      y = newY;
    }
    public Color getHatColor()
    {
      return hatColor;
    }
  }
