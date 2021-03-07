    import javax.swing.JOptionPane;
    import java.text.NumberFormat; 

    public class SentinelWhileLoop 
    {   
      public static void main(String[] args) 
      {  
       double balance = 1000.24;
       int numOfDeposits;
      double deposit, total, newBalance, averageDeposit;
      String input;
      NumberFormat us = NumberFormat.getCurrencyInstance();

       System.out.println("Your beginning balance was: "+ us.format(balance));   
      numOfDeposits = 0;
      total = 0.0;

      input = JOptionPane.showInputDialog("Enter a deposit, -1 to end");
      while( !input.equals("-1") ) //input is not "-1"
      {   	
        deposit = Double.parseDouble(input);
        total = total + deposit;
        numOfDeposits++; 
        input = JOptionPane.showInputDialog("Enter a deposit, -1 to end");
      }

      balance = balance + total;
      averageDeposit = total / numOfDeposits;

      System.out.println("The total of the " + numOfDeposits +
                         " deposits is "+ us.format(total));
      System.out.println("The average deposit was: " +
                          us.format(averageDeposit)); 
      System.out.println("Your new balance is: " + us.format(balance));
    }
  }
