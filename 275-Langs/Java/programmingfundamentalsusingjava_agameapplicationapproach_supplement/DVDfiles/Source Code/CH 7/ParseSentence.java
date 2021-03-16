   import javax.swing.*;

   public class ParseSentence 
   { 
     public static void main(String[] args) 
     {
       int upperCase = 0;
       int lowerCase = 0;
       int numeric = 0;
      int whitespace = 0;
      char c;

      String sentence = JOptionPane.showInputDialog("Enter a sentence");
      for(int i = 0; i < sentence.length(); i++)
      {   
        c = sentence.charAt(i);
        if(Character.isUpperCase(c))
        {
          upperCase++;
        }
        else if(Character.isLowerCase(c))
        {
          lowerCase++;
        }
        else if(Character.isDigit(c))
        {
          numeric++;
        }
        else if(Character.isWhitespace(c))
        {
          whitespace++;
        }
      }
      JOptionPane.showMessageDialog(null, "The sentence contains:\n" +
                                  upperCase + " Upper case letters,\n" +
                                  lowerCase + " Lower case letters,\n" +
                                  numeric + " Digits and\n" +
                                  whitespace + " Whitespace characters");
    }
  }
