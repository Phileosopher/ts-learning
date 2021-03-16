  import javax.swing.*;
  import java.io.*;

  public class FileChoosers 
  {
    public static void main(String[] args)      
    {
      JFileChooser fc;
      String path;
      int cancelApproveError;
      File file;

      //Demonstrate the ***OPEN*** file dialog box
      fc = new JFileChooser();
      cancelApproveError = fc.showOpenDialog(null);
      if(cancelApproveError == JFileChooser.APPROVE_OPTION) //Open clicked
      {
        file = fc.getSelectedFile(); //fetches file information
        path = file.getPath(); //returns the pat and file name
        System.out.println("The path to the file to be opened is:\n" + 
                            path);
      }
      else if(cancelApproveError == JFileChooser.CANCEL_OPTION) //canceled
      {
        System.out.println("The user canceled the file open operation");
      }
      else //an error
      {
        System.out.println("An error has occurred");
      }

      //Demonstrate the ***SAVE*** file dialog box 
      fc = new JFileChooser();
      cancelApproveError = fc.showSaveDialog(null);
      if(cancelApproveError == JFileChooser.APPROVE_OPTION) //Open clicked
      {
        file = fc.getSelectedFile();
        path = file.getPath();
        System.out.println("The path to the file to be written is:\n" +
                           path);
      }
      else if(cancelApproveError == JFileChooser.CANCEL_OPTION) //canceled
      {
        System.out.println("The user canceled the file save operation");
      }
      else //an error
      {
        System.out.println("An error has occurred");
      }
    }
  }
