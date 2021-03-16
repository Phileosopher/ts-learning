  import javax.swing.*;
  import java.text.NumberFormat;

  public class ArraysAndLoops 
  {    
    public static void main(String[] args) 
    {
      double[] price, salePrice;
      String s;
      int size;
      NumberFormat fm = NumberFormat.getCurrencyInstance();
      s = JOptionPane.showInputDialog("How many sale items?");
      size = Integer.parseInt(s);
      price = new double[size];
      salePrice = new double[size];

      for(int i = 0; i < size; i++)
      {
        s = JOptionPane.showInputDialog("Enter item " + (i + 1) +
                                        " 's price");
        price[i] = Double.parseDouble(s);
      }

      for(int i = 0; i < price.length; i++)
      {
        salePrice[i] = price[i] * 0.9;
        System.out.println("The sale price of item " + (i + 1)  + " is " +
                            fm.format(salePrice[i]));
      }			    	
    }
  }
