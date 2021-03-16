  import javax.swing.*;

  public class ParsingNumerics 
  {
    public static void main(String[] args) 
    {
      String input;
      String[] tokens;
      double sum = 0;
      String numerics = "";
      
      input = JOptionPane.showInputDialog("Enter a String containing " +
                                          "numerics");
      tokens = input.split(" +");
      for(int i = 0; i<tokens.length; i++)
      {
        try
        {
          sum = sum + Double.parseDouble(tokens[i]); //only numeric added
          numerics = numerics + tokens[i] + " + "; //build output string
        }
        catch(NumberFormatException e) //non-numeric
        {
          //prevents termination of application when exception is thrown
        }
      } //replace the last plus sign with an equals and produce the output
     numerics = numerics.substring(0, numerics.length() - 2) + "= ";
     JOptionPane.showMessageDialog(null, numerics + sum);
   }
 }
