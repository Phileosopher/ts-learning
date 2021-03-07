  import java.util.Scanner;
  public class ScannerConsoleInput 
  {
    public static void main(String[] args) 
    {
      Scanner consoleIn = new Scanner(System.in);
      String name;
      int age;
      double weight;

      System.out.print("Enter your name: ");
      name = consoleIn.nextLine();
      System.out.print("Enter your age: ");
      age = consoleIn.nextInt();
      System.out.print("Enter your weight: ");
      weight = consoleIn.nextDouble();
      System.out.println("Age: " + age + " Weight: " + weight +
                         " Name: " + name);
 
      System.out.print("\nEnter your age and weight on one line: ");
      age = consoleIn.nextInt();
      weight = consoleIn.nextDouble();
      System.out.print("Enter your name: ");
      consoleIn.nextLine(); // clears the enter keystroke from buffer
      name = consoleIn.nextLine();
      System.out.println("Age: " + age + " Weight: " + weight +
                         " Name: " + name);
    }
  }
