  import edu.sjcny.gpv1.*;
  import java.awt.*;
  import java.util.Random;

  public class ParallelArrays  extends DrawableAdapter
  {
    static ParallelArrays ge = new ParallelArrays(); 
    static GameBoard gb = new GameBoard(ge, "Parallel Object ArraysApp");
    static ParentSnowman[] parent;
    static SnowChild[] child; 

    public static void main(String[] args) 
    {
      String[] names = { "B", "D", "A", "E", "C"};
      parent = new ParentSnowman[5];
      child = new SnowChild[5];
      Random rn = new Random(500);
      int x, y;

      for(int i = 0;  i < 5;  i++)
      {
        x = 100 + rn.nextInt(500 - 100 - 30);
        y = 30 + rn.nextInt(500 - 30 - 30);
        parent[i] = new ParentSnowman(50, 50 + 90*i, names[i]);
        child[i] = new SnowChild(x, y, names[i]);
      }	
      showGameBoard(gb);
    }

    public void draw(Graphics g)
    {
      for(int i = 0; i<5; i++)
      {
        parent[i].show(g);
        child[i].show(g);
      }		
    }

    public void keyStruck(char key)
    {
      int x, y; 
      for(int i = 0; i< 5; i++)
      {	
        x = parent[i].getX();
        y = parent[i].getY();
        child[i].setX(x + 50);
        child[i].setY(y + 35);
      }
    }
  }
