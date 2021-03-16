import edu.sjcny.gpv1.*;

public class JCGameTemplateV7 extends DrawableAdapter
{   static JCGameTemplateV7 ge = new JCGameTemplateV7(); 
	static GameBoard gb = new GameBoard(ge, "Game Program");

    
    public static void main(String[] args) 
    {
    	
    	showGameBoard(gb);
    }
}
