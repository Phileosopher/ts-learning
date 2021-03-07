  import java.awt.*;

  public class TopHat extends GamePiece implements Drawable
  {

    public TopHat(int x, int y, Color hatColor, int w, int h)
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
    public boolean canDraw(int gbWidth, int gbHeight) //Completely on the
    {{                                                //game board
      if(x >= 6 && x + w <= gbWidth  
         &&
         y >= 30 && y + (int)(h * 1.1) <= gbHeight) 
      {
        return true;
      }
      else
      {
        return false;
      }  
    }
  }
