  import javax.swing.JOptionPane;

  public class EnhancedDialogBoxes 
  {    
    public static void main(String[] args) 
    {   
      String[] inputOptions = {"Freshman", "Sophomore",
                               "Junior", "Senior" };
      String s1, s2;

      // Titled message box with an error icon 
      JOptionPane.showMessageDialog(null, "The Disk I/O Failed", "ERROR", 
                                          JOptionPane.ERROR_MESSAGE);
      // Input box with a default input
      s1 = JOptionPane.showInputDialog("Enter your Class Standing",
                                       "Sophomore");

      // A Non-default icon titled Input box, a valid set of inputs
      s2 = (String) JOptionPane.showInputDialog(null, "Select your " + 
                                                      "class standing",
                                                      "Standing", 3,
                                                       null,
                                                       inputOptions, 
                                                       inputOptions[2]);
 
      System.out.println(s1 + " " + s2);
    }
  }
