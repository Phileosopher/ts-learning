  import java.math.BigInteger;
  import javax.swing.*;

  public class FibinacciTerm 
  {
    public static void main(String[] args) 
    {
      int n;
      BigInteger temp;
      BigInteger fnMinus1 = BigInteger.ONE;
      BigInteger fn = BigInteger.ONE;
      BigInteger longMaxValue = BigInteger.valueOf(Long.MAX_VALUE);

      String s = JOptionPane.showInputDialog("enter the term number");
      n = Integer.parseInt(s);
      for(int i = 3; i <= n; i++)
      {
        temp = fn;
        fn = fnMinus1.add(fn);
        fnMinus1 = temp;
      }
      System.out.println("f" + n + " = " + fn.toString());
      if(fn.compareTo(longMaxValue) > 0)
      {
        System.out.println("Which EXCEEDS the maximum value of " +
                           "type long");
      }
      else
      {
        System.out.println("Which does NOT exceed the maximum value of " +
                           "type long");
      }
    }
  }
