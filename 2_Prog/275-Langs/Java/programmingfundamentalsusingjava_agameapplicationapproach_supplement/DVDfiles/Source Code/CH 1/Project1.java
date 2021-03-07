  import edu.sjcny.gpv1.*;
  public class Project1 extends DrawableAdapter
  { 
    static Project1 ga = new Project1 ( ); 
    static GameBoard gb = new GameBoard(ga, "Frogger, by Bob");

    public static void main(String[] args) 
    {	
       showGameBoard(gb);
    } 
  }
