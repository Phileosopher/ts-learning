   import javax.swing.JOptionPane;
   import java.text.NumberFormat; 
   import java.util.Locale; 

  public class TotalingLoop 
   {   
    public static void main(String[] args) 
    { 
      double balance = 1000.24;
      int numOfDeposits;
      double deposit, total, newBalance, averageDeposit;
      String input;
      NumberFormat us = NumberFormat.getCurrencyInstance(Locale.US);

      System.out.println("Your beginning balance is: " + 
                          us.format(balance));   
      input = JOptionPane.showInputDialog("How Many Deposits?");
      numOfDeposits = Integer.parseInt(input);

      total = 0.0;
      for(int i = 1; i <= numOfDeposits;  i++)
      {
        input = JOptionPane.showInputDialog("Enter a deposit");
        deposit = Double.parseDouble(input);
        total = total + deposit;
      }
      balance = balance + total;
      averageDeposit = total / numOfDeposits;

      System.out.println("The total of the " + numOfDeposits +
                         " deposits is " + us.format(total));
      System.out.println("The average deposit was: " +
                          us.format(averageDeposit));   
      System.out.println("Your new balance is: " + us.format(balance));
    }
  }
