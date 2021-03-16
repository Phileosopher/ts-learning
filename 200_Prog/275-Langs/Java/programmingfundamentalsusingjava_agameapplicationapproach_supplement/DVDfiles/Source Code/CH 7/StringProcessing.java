  import javax.swing.*;

  public class StringProcessing
  {
    public static void main(String[] args)
    {
      String s1, s2;
      String[] sArray;
      int nWords;

      s1 = JOptionPane.showInputDialog("Enter a sentence, Please\n" +
                                       "Don't begin it with Hello,\n" +
                                       "don't include the word Tom.\n" + 
                                       "Hello will be removed, and \n" +
                                       "Tom replaced with XXX."); 
      sArray = s1.split(" +"); //stores each word in a separate element
      nWords = sArray.length; //the number of words

      s2 = new String(s1);
      if(s2.indexOf("Hello") == 0)
      {
        s2 = s2.substring(6);
      }
      s2 = s2.replaceAll("Tom", "XXX");

      JOptionPane.showMessageDialog(null, "There are " + nWords +
                                   " words in your sentence:\n" +
                                   s1 + "\nThe revised sentence is:\n" + 
                                   s2);
    }
  }
