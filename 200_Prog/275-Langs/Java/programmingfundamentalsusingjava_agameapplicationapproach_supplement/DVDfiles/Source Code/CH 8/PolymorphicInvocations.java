  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class PolymorphicInvocations extends DrawableAdapter
  { 
    static PolymorphicInvocations ge = new PolymorphicInvocations(); 
    static GameBoard gb = new GameBoard(ge, "Design Techniques");
    static RowBoatV2 rb1 = new RowBoatV2(50, 200, 120, Color.YELLOW, 4);
    static SailBoatV4 sb1 = new SailBoatV4(220, 200, 200, Color.GREEN, 200);
    static PowerBoat pb1 = new PowerBoat(50, 300, 200, Color.MAGENTA, 400);
    static Boat boat1, boat2, boat3;

    public static void main(String[] args) 
    {
      boat1 = rb1;
      boat2 = sb1;
      boat3 = pb1;    
      showGameBoard(gb);
    }
    
    public void draw(Graphics g)
    {
      boat1.show(g);
      boat2.show(g);
      boat3.show(g);
    }	
  }
