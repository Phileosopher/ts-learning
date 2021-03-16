  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class PolymorphicArrays extends DrawableAdapter
  {
    static PolymorphicArrays ge = new PolymorphicArrays(); 
    static GameBoard gb = new GameBoard(ge, "POLYMORPHIC ARRAYS");
    static RowBoatV2 rb;
    static SailBoatV4 sb;
    static PowerBoat pb;
    static Boat[] inventory = new Boat[9];

    public static void main(String[] args) 
    {
      for(int i = 0; i < 3; i++)		    
      {
        rb = new RowBoatV2(10 + i * 130, 75, 120, Color.YELLOW, i * 2 + 2);
        sb = new SailBoatV4(10 + i * 170, 250, 110 + i * 15, Color.GREEN,
                            200 + i * 20);
        pb = new PowerBoat(20 + i * 160, 350, 120 + i * 15, Color.MAGENTA,
                           400);
        inventory[i * 3] = rb;
        inventory[i * 3 + 1] = sb;
        inventory[i * 3 + 2] = pb;
      }

      showGameBoard(gb);
    }
    
    public void draw(Graphics g)
    {
      for(int i = 0; i < 9; i++)		    
      {
        inventory[i].show(g);	
      }                       	
    }	
  }
