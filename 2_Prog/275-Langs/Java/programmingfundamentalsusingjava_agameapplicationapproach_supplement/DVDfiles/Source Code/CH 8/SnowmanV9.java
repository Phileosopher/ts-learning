  import java.awt.*;
  import javax.swing.*; 

  public class SnowmanV9 extends GamePiece implements Drawable
  {
    public SnowmanV9(int x, int y, Color hatColor, int w, int h)
    {
      this.x = x;
      this.y = y;
      this.hatColor = hatColor;
      this.w = w;
      this.h = h;
    }
    public void show(Graphics g) 
    {
      g.setColor(Color.WHITE);
      g.fillOval(x + 20, y + 30, 40, 40); //head
      g.fillOval(x, y + 70, 80, 80); //body
      g.setColor(hatColor);
      g.fillRect(x + 30, y, 20, 30); //hat
      g.fillRect(x + 20, y + 30, 40, 2); //brim
    }
    public boolean canDraw(int gbWidth, int gbHeight) //Partially on the 
    {                                                 //game board
      if(x + w >= 6 && x <= gbWidth  
         &&
         y  + (int)(h * 1.1) >= 30 && y <= gbHeight) 
      {
        return true;	   		
      }
      else
      {
        return false;
      }  
    }
  }
