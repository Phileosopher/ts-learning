  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class ExtendingDataMembers extends DrawableAdapter
  { static ExtendingDataMembers ge = new ExtendingDataMembers (); 
    static GameBoard gb = new GameBoard(ge, "EXTENDING DATA MEMBERS");
    static RowBoat rb1 = new RowBoat(30, 150, 200);
    static RowBoat rb2 = new RowBoat(30, 250, 150);
    static SailBoatV2 sb1 = new SailBoatV2(260, 150, 200, Color.CYAN);
    static SailBoatV3 sb2 = new SailBoatV3(260, 300, 200, Color.YELLOW, 300);

    public static void main(String[] args) 
    {
      showGameBoard(gb);
    }

    public void draw(Graphics g)
    {
      rb1.show(g);
      rb2.show(g);
      sb1.show(g);
      sb2.show(g);
    }
  }
