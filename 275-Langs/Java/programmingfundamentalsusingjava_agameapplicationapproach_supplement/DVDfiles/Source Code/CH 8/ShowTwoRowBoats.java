  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class ShowTwoRowBoats extends DrawableAdapter
  { static ShowTwoRowBoats ge = new ShowTwoRowBoats(); 
    static GameBoard gb = new GameBoard(ge, "Show Two Row Boats");
    static RowBoat rb1 = new RowBoat(30, 150, 200);
    static RowBoat rb2 = new RowBoat(30, 250, 150);

    public static void main(String[] args) 
    {
      showGameBoard(gb);
    }
    public void draw(Graphics g)
    {
      rb1.show(g);
      rb2.show(g);
    }
  }
