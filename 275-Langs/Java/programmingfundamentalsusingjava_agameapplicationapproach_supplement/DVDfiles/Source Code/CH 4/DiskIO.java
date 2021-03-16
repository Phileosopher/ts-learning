  import java.util.Scanner; 
  import java.io.*;
 
  public class DiskIO 
  {    
    public static void main(String[] args) throws IOException
    { 
      File fileObject = new File("data.txt"); // input 
      Scanner fileIn = new Scanner(fileObject);
      FileWriter fileWriterObject = new FileWriter("data.txt");// output
      PrintWriter fileOut = new PrintWriter(fileWriterObject, false); 
       
      String name = "Nora Smith";
      int age = 5;
      double weight = 35.4;

      // write three data items to the disk file
      fileOut.println(age + " " + weight);
      fileOut.println(name);
      fileOut.close();

      //read the data from the disk file 
      age = fileIn.nextInt();
      weight = fileIn.nextDouble();
      fileIn.nextLine(); // clears New Line after a numeric from the buffer
      name = fileIn.nextLine();
      fileIn.close();
       
      System.out.println("Age: " + age + " Weight: " + weight +
                         " Name: " + name);
    }
  }
