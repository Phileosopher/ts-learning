  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class InheritanceBasics extends DrawableAdapter
  { static InheritanceBasics ge = new InheritanceBasics(); 
    static GameBoard gb = new GameBoard(ge, "Inheritance Basics");
    static RowBoat rb1 = new RowBoat(30, 150, 200);
    static RowBoat rb2 = new RowBoat(30, 250, 150);
    static SailBoat sb1 = new SailBoat(260, 150, 200, Color.CYAN);

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
