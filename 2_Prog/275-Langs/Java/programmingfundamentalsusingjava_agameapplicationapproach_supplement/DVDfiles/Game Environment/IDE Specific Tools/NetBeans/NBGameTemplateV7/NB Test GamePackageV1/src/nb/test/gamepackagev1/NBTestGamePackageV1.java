
package nb.test.gamepackagev1;
import edu.sjcny.gpv1.*;

public class NBTestGamePackageV1 extends DrawableAdapter
{   static NBTestGamePackageV1 ge = new NBTestGamePackageV1(); 
    static GameBoard gb = new GameBoard(ge, "Snowman by Bill McAllister");
    public static void main(String[] args) 
    {
          showGameBoard(gb);
// TODO code application logic here
    }
}
