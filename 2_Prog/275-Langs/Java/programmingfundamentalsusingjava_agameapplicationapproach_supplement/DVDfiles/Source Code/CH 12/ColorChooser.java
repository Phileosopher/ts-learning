  import javax.swing.*;
 
  public class ColorChooser 
  {
   public static void main(String[] args)      
   {
     String title = "File and Color Chooser Dialogs";
     ColorChooserWindow window = new ColorChooserWindow(title);
     window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		
     window.setVisible(true);
   }
  }
