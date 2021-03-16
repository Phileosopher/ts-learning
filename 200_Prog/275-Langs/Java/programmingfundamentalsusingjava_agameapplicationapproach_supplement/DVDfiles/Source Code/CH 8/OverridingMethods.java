  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class OverridingMethods extends DrawableAdapter
  { static OverridingMehtods ge = new OverridingMethods(); 
    static GameBoard gb = new GameBoard(ge, "Inheritance Basics");
    static RowBoat rb1 = new RowBoat(30, 150, 200);
    static RowBoat rb2 = new RowBoat(30, 250, 150);
    static SailBoatV2 sb1 = new SailBoatV2(260, 150, 200, Color.CYAN);

    public static void main(String[] args) 
    {
      showGameBoard(gb);
    }

    public void draw(Graphics g)
    {
      rb1.show(g);
      rb2.show(g);
      sb1.show(g);
    }
  }
