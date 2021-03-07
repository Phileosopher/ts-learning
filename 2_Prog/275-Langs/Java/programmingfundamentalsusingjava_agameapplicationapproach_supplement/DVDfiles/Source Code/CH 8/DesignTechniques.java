  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class DesignTechniques extends DrawableAdapter
  { 
    static DesignTechniques ge = new DesignTechniques(); 
    static GameBoard gb = new GameBoard(ge, "Design Techniques");
    static RowBoatV2 rb1 = new RowBoatV2(50, 200, 120, Color.YELLOW, 4);
    static SailBoatV4 sb1 = new SailBoatV4(220, 200, 200, Color.GREEN, 200);
    static PowerBoat pb1 = new PowerBoat(50, 300, 200, Color.MAGENTA, 400);
   
    public static void main(String[] args) 
    {
   	  showGameBoard(gb);
    }
   
    public void draw(Graphics g)
    {
      rb1.show(g);
      sb1.show(g);
      pb1.show(g);
    }
  }	
