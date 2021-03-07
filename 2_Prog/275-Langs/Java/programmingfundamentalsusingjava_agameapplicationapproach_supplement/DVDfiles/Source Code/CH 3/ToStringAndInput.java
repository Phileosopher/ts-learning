   import edu.sjcny.gpv1.*;
   import java.awt.Graphics;
   
   public class ToStringAndInput extends DrawableAdapter
   {   
     static ToStringAndInput ge = new ToStringAndInput(); 
     static GameBoard gb = new GameBoard(ge,"toString And input Methods");
     static SnowmanV5 sm1 = new SnowmanV5(7, 30);
     static SnowmanV5 sm2 = new SnowmanV5(460, 420);

     public static void main(String[] args) 
     {
       System.out.println("sm1's\n" + sm1.toString());
       System.out.println("sm2's\n" + sm2.toString());
       showGameBoard(gb);
       sm1.input();
       sm2.input();
       showGameBoard(gb);
     }
 
     public void draw(Graphics g)
     {
       sm1.show(g);
       sm2.show(g);
     }
   }
