      import edu.sjcny.gpv1.*;
      import java.awt.*;
      public class ClassAndObjectBasics extends DrawableAdapter
      {
         static ClassAndObjectBasics ge = new ClassAndObjectBasics(); 
         static GameBoard gb = new GameBoard(ge, "Class & Object Basics");
         static Person mary, kate;
    
         public static void main(String[] args) 
        {  mary = new Person();
           kate = new Person();
        
           System.out.println(mary);
           System.out.println(kate);
        
           showGameBoard(gb);
        }
    	
        public void draw(Graphics g)
        {
           g.drawString(mary.toString(), 210, 100);
           g.drawString(kate.toString(), 210, 120);
        }      
     }
