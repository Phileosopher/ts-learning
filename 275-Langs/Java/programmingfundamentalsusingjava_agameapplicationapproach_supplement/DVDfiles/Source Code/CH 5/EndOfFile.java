  import java.util.Scanner; 
  import java.io.*;
  import java.text.NumberFormat;

  public class EndOfFile 
  {
    public static void main(String[] args) throws IOException
    {
      double balance = 1000.24;
      int numOfDeposits;
      double deposit, total, newBalance, averageDeposit;
      NumberFormat us = NumberFormat.getCurrencyInstance();
      File fileObject = new File("c:/data.txt");
      Scanner fileIn = new Scanner(fileObject);

      numOfDeposits = 0;
      total = 0.0;

      System.out.println("Your beginning balance is: " +
                          us.format(balance));
      while(fileIn.hasNext()) //more data to process 
      { 
        deposit = fileIn.nextDouble();
        total = total + deposit;
        numOfDeposits++; 
      }
      balance = balance + total;
      averageDeposit = total / numOfDeposits;

      System.out.println("The total of the " + numOfDeposits + 
                         " deposits is " + us.format(total));
      System.out.println("The average deposit was: " +
                          us.format(averageDeposit));   
    System.out.println("Your new balance is: " + us.format(balance));
    fileIn.close();
    }
  }
