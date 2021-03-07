  import java.awt.*;
  import java.applet.*;
  import javax.swing.*;
  import java.util.Random;
  import java.awt.event.*;

  public class GuessingGame extends JApplet implements ActionListener 
  {
    boolean firstClick = true;
    int firstClickValue = 0;
    int firstClickIndex = 0;
    int secondClickIndex = 0;
    int errorCount = 0;
    boolean correct = false;
    int[] values = new int[16];
    JButton b = new JButton();
    JButton[]cell;
    JLabel errors = new JLabel("Errors: ");
    JLabel numberOfErrors = new JLabel("0");
    JButton begin = new JButton("Begin");
    JButton reset = new JButton("Reset");
    Timer timer1 = new Timer(2000, new TimerHandler());

    public void init() 
    {
      cell = new JButton[16]; //the number buttons
 
      setLayout(new GridLayout(5, 4)); //override default BorderLayout

      //set properties of GUI compoments
      errors.setHorizontalAlignment(JLabel.RIGHT);       
      errors.setFont(new Font("Serif", Font.BOLD, 30));
      numberOfErrors.setFont(new Font("Serif", Font.BOLD, 30));

      //add event handlers to listener lists
      begin.addActionListener(new BeginResetHandler());
      reset.addActionListener(new BeginResetHandler());

      //create number buttons, set properties, register event handlers
      for(int i = 0; i < 16; i++)
      {
        cell[i] = new JButton("0");
        cell[i].setFont(new Font("Serif", Font.BOLD, 40));
        cell[i].addActionListener(this);  	
        add(cell[i]);
      }

      //add the lower buttons and labels
      add(begin);
      add(errors);
      add(numberOfErrors);
      add(reset);

      intializeGame();
    }    

    public void intializeGame()
    {
      generateNumbers();
      numberOfErrors.setText("0");
      errorCount = 0;
      for(int i = 0; i < 16; i++)
      {
        cell[i].setText(Integer.toString(values[i]));
        cell[i].setForeground(Color.BLACK);
      }
    }

    public void generateNumbers() //generates buttons' numbers 
    {
      Random rn = new Random();
      int number = 0;
      int cellNumber = 0;
      boolean done;

      for(int i = 1; i <= 16; i++) //all number buttons 
      {
        values[i-1] = i % 8 + 1; //place numbers 1->8 twice
      }
      for(int i = 0; i < 16; i++) //all number buttons
      {
        number = rn.nextInt(15); 
        swap(values, i, number); //swap button value with a random button
      }
    }

    public void swap(int[] array, int indx1, int indx2)
    {
      int temp;
      temp = array[indx1];
      array[indx1] = array[indx2];
      array[indx2] = temp; 
    }

     //event handlers ***************************************
     public class BeginResetHandler implements ActionListener
     {
       public void actionPerformed(ActionEvent e)
       {
        if(e.getSource() == begin) // start the game 
        {
          for(int i = 0; i < 16; i++)
          {
            cell[i].setText(" "); //hide the numbers
          }
        }
        else //generate and a new game
        {
          intializeGame();
       }
      }
    }  	

    public void actionPerformed(ActionEvent e) //number buttons' handler
    {
      if(firstClick) //show the number
      {
        for(int i = 0; i<16; i++) //all number buttons
        {
          if(e.getSource() == cell[i]) //button clicked found
          {
            cell[i].setText(Integer.toString(values[i]));
            firstClick = false;
            firstClickValue = values[i];
            firstClickIndex = i;
            break;
          }
        }
      }
      else //second click processing
      {
        timer1.start(); //two seconds
        for(int i = 0; i<16; i++) //all number buttons
        {
          if(e.getSource() == cell[i]) //button clicked found
          {
            cell[i].setText(Integer.toString(values[i]));
            firstClick = true;
            secondClickIndex = i;
            if(firstClickValue == values[i]) //correct match
            {
              correct = true;
              cell[firstClickIndex].setForeground(Color.BLUE);
              cell[secondClickIndex].setForeground(Color.BLUE);
            }
            else //incorrect match
            {
              correct = false;
              errorCount++;
              numberOfErrors.setText(Integer.toString(errorCount));
            }
            break;
          }
        }
      }
    }

    public class TimerHandler implements ActionListener
    {
      public void actionPerformed(ActionEvent e) //Timer's event handler
      { 
        if(correct == false) //no match
        {
          timer1.stop(); //after a two second pause
          cell[firstClickIndex].setText(" "); //hide the numbers
          cell[secondClickIndex].setText(" ");
        }
      }
    }
  }
