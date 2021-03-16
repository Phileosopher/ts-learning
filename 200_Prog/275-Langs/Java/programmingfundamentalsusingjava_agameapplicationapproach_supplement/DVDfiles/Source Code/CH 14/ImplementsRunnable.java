  public class ImplementsRunnable implements Runnable
  {
    private String name;
    private int nLines;

    public ImplementsRunnable(String name) 
    {
       this.name = name;
    }

    public void run() //A thread's entry point
    {
      System.out.println(name + " is executing");
    }
  }
