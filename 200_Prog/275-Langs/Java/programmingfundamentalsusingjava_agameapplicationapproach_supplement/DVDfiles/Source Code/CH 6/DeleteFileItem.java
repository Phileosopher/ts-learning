  import java.util.Scanner; 
  import java.io.*;
  import javax.swing.*;

  public class DeleteFileItem 
  {
    public static void main(String[] args) throws IOException
    { 
      double[] data;
      double deletedItem;
      int count = 0; 

      //Step 1: Open the file, read the number of items, allocate the array
      File fileObject = new File("scores.txt");  
      Scanner fileIn = new Scanner(fileObject);
      count = fileIn.nextInt();
      data = new double[count];

      //Step 2: Read all of the file's data items into the array
      for(int i = 0; i < count; i++)
      {
        data[i] = fileIn.nextDouble();
      }

      //Step 3: Close the file
      fileIn.close();

      //Step 4: Delete and recreate the file
      FileWriter fileWriterObject = new FileWriter("scores.txt");
      PrintWriter fileOut = new PrintWriter(fileWriterObject, false);
      fileOut.println(count - 1); 

      //Step 5: write the elements of the array, less the deleted item
      String s = JOptionPane.showInputDialog("enter score to delete");
      deletedItem = Double.parseDouble(s);
      for(int i = 0; i < count; i++)
      {
        if(data[i] != deletedItem)
        {
          fileOut.println(data[i]);
        }
      }

      //Step 6: Close the file
      fileOut.close();
    }
  }
