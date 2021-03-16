  import edu.sjcny.gpv1.*;
  import java.awt.*;

  public class RecursiveFractal extends DrawableAdapter
  {   
    static RecursiveFractal ge = new RecursiveFractal(); 
    static GameBoard gb = new GameBoard(ge, "RECURSIVE FRACTAL");
    static Point p1 = new Point(250, 70); //vertices of the 1st triangle
    static Point p2 = new Point(25, 460);
    static Point p3 = new Point(475, 460);

    public static void main(String args[])
    {
      showGameBoard(gb);
    }
    
    public void draw(Graphics g)
    {   
      g.setColor(Color.BLUE);
      drawSierpinsky(8, p1, p2, p3, g);
    }

    public static Point midPoint(Point p1, Point p2)
    {
      Point midPoint = new Point();
      midPoint.y = p1.y + (p2.y - p1.y)/2;
      midPoint.x = p1.x + (p2.x - p1.x)/2;
      return midPoint;      
    }

    public static void drawSierpinsky(int iterations, Point p1, Point p2,
                                      Point p3, Graphics g)
    {
      if(iterations == 0) //base case
      {
        return;
      }
      //general solution
      g.drawLine(p1.x, p1.y, p2.x, p2.y); //draw a triangle
      g.drawLine(p2.x, p2.y, p3.x, p3.y);
      g.drawLine(p3.x, p3.y, p1.x, p1.y);
      iterations--;
      //reduced problems to draw top, left & right side triangles recursively 
      drawSierpinsky(iterations, p1, midPoint(p1,p2), midPoint(p1,p3), g);
      drawSierpinsky(iterations, p2, midPoint(p2,p1), midPoint(p2,p3), g);
      drawSierpinsky(iterations, p3, midPoint(p3,p1), midPoint(p3,p2), g); 
    }
  }
