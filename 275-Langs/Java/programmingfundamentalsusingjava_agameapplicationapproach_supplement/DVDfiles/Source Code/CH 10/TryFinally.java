  import java.io.*;
  import javax.swing.*;

  public class TryFinally 
  {
    public static void main(String[] args) 
    {
      String data = JOptionPane.showInputDialog("Enter a data item");	
      try
      { 
        appendDataItem("dataFile.txt", data);
      }
      catch(IOException e)
      {
        System.out.println("There were problems writing to the file");
        System.exit(0);	
      }
    }

    public static void appendDataItem(String fileName,
                                      String dataItem) throws IOException
    {
      PrintWriter fileOut = null;	
      try
      { 
        FileWriter fileWriterObj = new FileWriter(fileName, true);
        fileOut = new PrintWriter(fileWriterObj);
        fileOut.println(dataItem);
      }
      finally
      {
        fileOut.close();
      }
      System.out.println("The data was written to the file");
    }
  }
