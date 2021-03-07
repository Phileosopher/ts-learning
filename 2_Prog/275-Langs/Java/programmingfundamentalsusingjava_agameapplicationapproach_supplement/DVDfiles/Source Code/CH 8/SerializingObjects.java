  import edu.sjcny.gpv1.*;
  import java.awt.*;
  import java.io.*; 

  public class SerializingObjects extends DrawableAdapter
  {
    static SerializingObjects ge = new SerializingObjects(); 
    static GameBoard gb = new GameBoard(ge, "SERIALIZING OBJECTS");
    static RowBoatV2 rb;
    static SailBoatV4 sb;
    static PowerBoat pb;
    static Boat[] inventory = new Boat[9];

    public static void main(String[] args) 
    {
      for(int i = 0; i < 3; i++)		    
      {
        rb = new RowBoatV2(10 + i * 130, 75, 120, Color.YELLOW, i * 2 + 2);
        sb = new SailBoatV4(10 + i * 170, 250, 110 + i * 15, Color.GREEN,
                            200 + i * 20);
        pb = new PowerBoat(20 + i * 160, 350, 120 + i * 15, Color.MAGENTA,
                           400);
        inventory[i * 3] = rb;
        inventory[i * 3 + 1] = sb;
        inventory[i * 3 + 2] = pb;
      }

      showGameBoard(gb);
    }
    
    public void draw(Graphics g)
    {
      for(int i = 0; i < 9; i++)		    
      {
        if(inventory[i] != null)
        {
          inventory[i].show(g);	
        }	
      }                       	
    }	

    public void upButton() //delete the RAM based inventory
    { 
      for(int i = 0; i < 9; i++)		    
        {
           inventory[i] = null;
        }
    }    
    public void rightButton() //output inventory to the file
    {
      try
      { FileOutputStream fos = new FileOutputStream("Inventory");
        ObjectOutputStream outFile = new ObjectOutputStream(fos);

        for(int i = 0; i < 9; i++)
        {
          if(inventory[i] != null)
          {
            outFile.writeObject(inventory[i]);	
          }
        }
        outFile.close();
      }
      catch(IOException e)
      {
      }
    }
  
    public void leftButton() //input inventory from the file
    {
      try					
      { FileInputStream fis = new FileInputStream("Inventory ");
        ObjectInputStream inFile = new ObjectInputStream(fis);
       
        for(int i = 0; i < 9; i++)		    
        {
          inventory[i] = (Boat) inFile.readObject();	
        }
        inFile.close();
      }
      catch(IOException e)
      {
      }
      catch(ClassNotFoundException e)
      {
      }
    }
  }
