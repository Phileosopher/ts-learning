  import javax.swing.*;

  public class ProcessingExceptions 
  {   
    public static void main(String[] args) 
    {
      String s;
      int a, b;
      int quotient = 0;
      int remainder = 0;
 
      s = JOptionPane.showInputDialog("This program calculates a / b " +
                                      "\nEnter the value of a" );
      a = Integer.parseInt(s);
      s = JOptionPane.showInputDialog("Enter the value of b" );
      b = Integer.parseInt(s);
      
      for(int i=1; i<=3; i++) //three attempts to divide a and b
      {   
        try
        {
          quotient = a / b; //could throw an ArithmeticException
          remainder = a % b;
          break; //ends the for loop and Line 43 executes next
        } 
        catch(ArithmeticException e)
        {
          if(i != 3) //three attempts to divide have not been made
          {
            s = JOptionPane.showInputDialog("A divisor cannot be zero." +
                                            "\nPlease re-enter it");
            b = Integer.parseInt(s); 
          }
          else
          {
            JOptionPane.showMessageDialog(null, "Division by zero " +
                                                "is undefined \n" +
                                                "The program is ending");
            System.exit(0); //terminate the program
          }
        } //end of the try-catch construct
      } 	
      JOptionPane.showMessageDialog(null, a + " / " + b + " = " +
                                          quotient + ", with a " +
                                          "remainder of " + remainder);
    }
  }
