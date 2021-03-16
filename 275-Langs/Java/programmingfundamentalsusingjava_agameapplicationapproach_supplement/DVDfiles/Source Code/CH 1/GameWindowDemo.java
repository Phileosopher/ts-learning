import edu.sjcny.gpv1.*;
public class GameWindowDemo extends DrawableAdapter
{ 
  static GameWindowDemo ga = new GameWindowDemo( ); 
  static GameBoard gb = new GameBoard(ga, "The Game Window");

  public static void main(String[] args) 
  {	
    showGameBoard(gb);
  } 
}
