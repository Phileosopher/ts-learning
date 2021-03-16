  public class Counter 
  {   
    private static int counter = 0;
 
    public int getCounter()
    {
      return counter;
    }

    public void setCounter(int value)
    {
      counter = value;
    }

    public static void outputCounter()
    {
      System.out.println(counter);
    }
  }
