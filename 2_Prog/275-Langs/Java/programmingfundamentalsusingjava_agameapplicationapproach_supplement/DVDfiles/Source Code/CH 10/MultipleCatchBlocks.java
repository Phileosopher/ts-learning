  import javax.swing.*;

  public class MultipleCatchBlocks 
  {
    public static void main(String[] args) 
    {
      String sa, sb;
      int a = 0;
      int b = 0;
      int quotient = 0;
      int remainder = 0;
      
      try
      {  
        sa = JOptionPane.showInputDialog("This program calculates " +
                                         "a / b\nEnter the value of a" );
        a = Integer.parseInt(sa); //throws a NumberFormatException
        sb = JOptionPane.showInputDialog("Enter the value of b" );
        b = Integer.parseInt(sb); //throws a NumberFormatException
        quotient = a / b;
        remainder = a % b;
      } //end of the try block
      catch(ArithmeticException e) //process divide by zero
      {
        JOptionPane.showMessageDialog(null, "Division by zero " +
                                            "is undefined. \n" +
                                            "\nThe program is ending");
        System.exit(0);
      } //end of the first catch block
      catch(NumberFormatException e) //process non-integer input
      { 
        JOptionPane.showMessageDialog(null, "Enter only digits " +
                                     "for the operands." +
                                     "\nThe program is ending");
        System.exit(0);
      } //end of the second catch block
      JOptionPane.showMessageDialog(null, a + " / " + b + " = " +
                                          quotient + ", with a " +
                                          "remainder of " + remainder);
    }
  }
