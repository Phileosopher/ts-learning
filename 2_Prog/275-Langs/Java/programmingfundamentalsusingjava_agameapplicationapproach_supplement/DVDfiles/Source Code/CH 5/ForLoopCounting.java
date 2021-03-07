  import javax.swing.*;
  public class ForLoopCounting 
  { 
    public static void main(String[] args) 
    { int start, end, increment;
      String input;
      input = JOptionPane.showInputDialog("Enter the starting value:");
      start = Integer.parseInt(input);
      input = JOptionPane.showInputDialog("Enter the ending value: ");
      end = Integer.parseInt(input);
      input = JOptionPane.showInputDialog("Count by?: ");
      increment = Integer.parseInt(input);
 
      System.out.println("Counting from " + start + " to " + end +
                         " by " + increment + "s:");
      for(int i=start; i<=end; i=i+increment)
      {
        System.out.println(i);
      }	
    }
  }
