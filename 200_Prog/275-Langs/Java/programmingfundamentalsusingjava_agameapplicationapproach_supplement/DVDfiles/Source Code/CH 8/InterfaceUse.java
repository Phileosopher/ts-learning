  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class InterfaceUse extends DrawableAdapter
  { 
    static InterfaceUse ge = new InterfaceUse(); 
    static GameBoard gb = new GameBoard(ge, "INTERFACES", 700, 700);
    static Drawable[] items = new Drawable[6];

    public static void main(String[] args) 
    {
      items[0] = new TopHat(-10, 30, Color.BLUE, 51, 60); //part off
      items[1] = new TopHat(350, 360, Color.BLACK, 51, 60);
      items[2] = new TopHat(600, 640, Color.GREEN, 51, 60); //part off
      items[3] = new SnowmanV9(-10, 120, Color.BLUE, 74, 152); //part off
      items[4] = new SnowmanV9(200, 360, Color.BLACK, 80, 152);
      items[5] = new SnowmanV9(400, 640, Color.GREEN, 80, 152); //part off
      showGameBoard(gb);
    }
    
    public void draw(Graphics g)
    {  
      for(int i = 0; i < items.length; i++)
      {
        if(items[i].canDraw(700, 700))
        { 
          items[i].show(g);
        }
      }
    }
  }
