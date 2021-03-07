  import edu.sjcny.gpv1.*;
  import java.awt.*;
  import javax.swing.*;

  public class ObjectAndClass extends DrawableAdapter
  { static ObjectAndClass ge = new ObjectAndClass(); 
    static GameBoard gb = new GameBoard(ge, "getClass and getName Methods");
    static Boat[] inventory = new Boat[9];

    public static void main(String[] args) 
    {
        String s;
    	
        // Polymorphic array
        for(int i = 0; i < 3; i++)	
        {
          inventory[i*3] = new RowBoatV2(10 + i*130, 75, 120, 
                                         Color.YELLOW, i*2 + 2);
          inventory[i*3 + 1] = new SailBoatV4(10 + i*170, 250 , 110+ i *15,
                                              Color.GREEN, 200 + i*20);
          inventory[i*3 + 2] = new PowerBoat(20 + i*160, 350 , 120+ i *15,
                                             Color.MAGENTA, 400);
        }

        s = JOptionPane.showInputDialog("Interested in, a RowBoatV2," +
                                        "\na SailBoatV4, or a PowerBoat?");
        for(int i = 0; i < inventory.length; i++)		    
        {
            if(inventory[i].getClass().getName().equalsIgnoreCase(s))
            {
              System.out.println(inventory[i].toString());
            }
        }
        showGameBoard(gb);
    }
  
    public void draw(Graphics g)
    {
      for(int i = 0; i < 9; i++)
      {
        inventory[i].show(g);
      }   
    }
  }
