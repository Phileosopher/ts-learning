  import javax.swing.*;

  public class ExtendsThread extends Thread
  {
    private String name;

    public ExtendsThread(String name) 
    {
      super();
      this.name = name;
    }

    public void run() //A thread's entry point
    {
      System.out.println(name + " is executing");

      String answer  = JOptionPane.showInputDialog("What is 23 + 57 ?");
      if(answer.equals("80"))
      {
        System.out.println("Correct, 23 + 57  = 80");
      }
      else
      {
        System.out.println("Incorrect, 23 + 57  = 80");
      }
    }
  }
