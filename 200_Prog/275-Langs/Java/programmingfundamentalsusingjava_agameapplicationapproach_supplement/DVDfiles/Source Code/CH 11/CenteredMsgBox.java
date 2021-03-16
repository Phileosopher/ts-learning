  import edu.sjcny.gpv1.*;
  import javax.swing.JOptionPane;

  public class CenteredMsgBox extends DrawableAdapter
  {   
    static CenteredMsgBox ge = new CenteredMsgBox(); 
    static GameBoard gb = new GameBoard(ge, "My Game");

    public static void main(String args[])
    {
      showGameBoard(gb);
      JOptionPane.showMessageDialog(gb, "A Messages Box Centered " +
                                        "in the Game Board Window");
      showGameBoard(gb);
    }
  } 
