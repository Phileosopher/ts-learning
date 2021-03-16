  import javax.swing.*;
  import java.text.DecimalFormat;

  public class FibonacciDynamic
  { 
    static long invocations = 0;
    static long[] data = new long[101];

    public static void main(String[] args)
    { 
      DecimalFormat f = new DecimalFormat("#,###");

      String s = JOptionPane.showInputDialog("Enter the term number," +
                                             " n, to be evaluated:" +
                                               " 1<= n <=100");
      int n = Integer.parseInt(s);

      System.out.println("fn = " + f.format(fib(n)) + 
                         "\ncalculated making " + f.format(invocations) +
                         " invocations");
      invocations = 0;
      System.out.println();
      System.out.println("fn = " + f.format(fibDynamic(n)) + 
                         "\ncalculated making " + f.format(invocations) +
                         " invocations");
    }

    public static long fib(int n)
    {     
      long rp1, rp2;
      invocations++;

      if(n == 1 || n == 2) //defined base cases
      {
        return 1;
      }
      else //general solution
      { rp1 = fib(n-1); //calculate first reduced problem
        rp2 = fib(n-2); //calculate second reduced problem 
        return rp1 + rp2;
      }
    }

    public static long fibDynamic(int n)
    {     
      long rp1 = 0;
      long rp2, gs;
      invocations++;

      if(n == 1 || n == 2) //defined base cases
      {
        data[n] = 1;
        return 1;
      }
      else if(data[n] != 0) //dynamic programming base case
      {
        return data[n];
      }
      else //general solution
      {
        if(data[n-1] == 0) //calculate f1rst reduced problem
        {  
          data[n-1] = fibDynamic(n-1);
        }
        rp1 = data[n-1];
        if(data[n-2] == 0) //calculate second reduced problem
        {  
          data[n-2] = fibDynamic(n-2);
        }
        rp2 = data[n-2];
        gs = rp1 + rp2;
        return gs;
    }
    }
  }
