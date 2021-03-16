    import edu.sjcny.gpv1.*;
    import java.awt.*;
    import javax.swing.*;

    public class ArrayAlgorithms extends DrawableAdapter
    {   
      static ArrayAlgorithms ge = new ArrayAlgorithms(); 
      static GameBoard gb = new GameBoard(ge, "Array Algorithms");
      static ParentSnowman[] parent;  
      static SnowChild[] child;
 
    public static void main(String[] args) 
    { 	
      String name;
      parent = new ParentSnowman[5];
      child = new SnowChild[5];

      for(int i = 0; i < 5; i++)
      {
        name = JOptionPane.showInputDialog("enter a family name");
        name = name.toUpperCase();
        child[i] = new SnowChild(50 + 60, 80 + 90 * i, name);
        parent[i] = new ParentSnowman(50, 50 + 90 * i, name);
      }
      showGameBoard(gb);
    }

    public void draw(Graphics g)
    {
      for(int i = 0; i<5; i++)
      {
        if(parent[i].getVisible() == true)	
        { parent[i].show(g);
          child[i].show(g);
        } 
      }
    }

    public void keyStruck(char key)
    {
      int index;

      String sKey = Character.toString(key);
      index = findValue(parent, sKey);
      if(index != -1) //name is valid, reverse family’s visibility 
      {
        if(parent[index].getVisible() == true)
        {
          parent[index].setVisible(false);
        }
        else
        {
          parent[index].setVisible(true);
        }
      }

      if (key == 'U') //up arrow struck, reverse visibility of min name
      {
        index = findMin(parent); //index of first family in alphabetic order
        if(parent[index].getVisible() == true)
        {
          parent[index].setVisible(false);
        }
        else
        {
          parent[index].setVisible(true);
        }
      }
      if(key == 'S') //sort the families
      {
        selectionSort(parent);
      }
    }

    public static int findValue(ParentSnowman[] parent, String targetValue)
    {
      int elementNumber = -1;
      for(int i = 0; i< parent.length; i++)
      {
        if(parent[i].getName().equalsIgnoreCase(targetValue))
        {     
          elementNumber = i;
          break;
        }
      }
      return elementNumber;
    }
    
    public static int findMin(ParentSnowman[] parent)
    {
      String min = parent[0].getName();
      int elementNumber = 0;
      for(int i = 1; i <  parent.length; i++)
      {
        if(parent[i].getName().compareToIgnoreCase(min) <  0)
        {
          min = parent[i].getName();
          elementNumber = i;
        }
      }
      return elementNumber;
    }
 
    public static void selectionSort(ParentSnowman[] parent)
    {
      int iMin, tempInt;
      ParentSnowman tempParent;
      SnowChild tempChild;
      String min;

      for (int j = 0; j < parent.length; j++) 
      {     
        min = parent[j].getName();
        iMin = j;
        for (int i = j+1; i < parent.length; i++) 
        {
          if (parent[i].getName().compareToIgnoreCase(min) <  0) 
          {
            min = parent[i].getName();
            iMin = i;
          }
        }
        if ( iMin != j ) //swap element j with minimum element
        {
          tempParent = parent[j]; //swap array references
          parent[j] = parent[iMin];
          parent[iMin] = tempParent;
          tempChild = child[j];
          child[j] = child[iMin];
          child[iMin] = tempChild;

          tempInt = parent[j].getY(); //swap Y positions
          parent[j].setY(parent[iMin].getY());
          parent[iMin].setY(tempInt);
          child[j].setY(parent[j].getY() + 30);
          child[iMin].setY(parent[iMin].getY() + 30);
        }
      }
    }
  }
