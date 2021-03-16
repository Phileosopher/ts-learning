  import javax.swing.JOptionPane;

  public class MethodsAndParms 
  {  static int a = 10; // Two class level variables
     static int b; 

     public static void main(String[] args) 
     {
        int desiredAge, first, second, difference; // local Variables
   
       desiredAge = inputInteger("You are " + a + " years old" +
                                 "\nHow old do you wish you were?");
       difference = dif(desiredAge, a);
       JOptionPane.showMessageDialog(null, + "Only " + difference +
                                             " Years to go");

       first = inputInteger("Enter the first number to swap");
       second = inputInteger("Enter the second number to swap");
       swapParameters(first, second);
       JOptionPane.showMessageDialog(null, "Swapped using parameters: " +
                                            first + " " + second);

       a = inputInteger("Enter the first number to swap");
       b = inputInteger("Enter the second number to swap");
       swapClassLevels();
       JOptionPane.showMessageDialog(null, "Swapped using class levels: " +
                                            a + " " + b);
    }

    static int inputInteger(String prompt)
    {
       int a; // a local variable
       String sInput = JOptionPane.showInputDialog(prompt);
       a = Integer.parseInt(sInput);
       return a;
    }

    static int dif(int desiredAge, int a)
    {
       return desiredAge - a;
    }

    static void swapParameters(int a, int b)
    {
       int temp = a;
       a = b;
       b = temp;
    }

    static void swapClassLevels()
    {
     int temp = a;
     a = b;
     b = temp;
    }
 }
