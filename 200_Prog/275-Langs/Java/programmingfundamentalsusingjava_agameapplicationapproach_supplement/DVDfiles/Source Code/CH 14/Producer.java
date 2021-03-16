  import java.util.Random;

  public class Producer implements Runnable
  {
    private Buffer sharedData;
    private Random delay = new Random();

    public Producer(Buffer sharedData) 
    {
      this.sharedData = sharedData;
    }

    public void run()
    {
      for(int i = 1; i <= 10; i++)
      { 
        try
        {
          Thread.sleep(delay.nextInt(10) + 1); //simulate data processing 
        }
        catch(InterruptedException e)
        {
        }
        sharedData.setData(i);
        System.out.println("Produced " + i);
      }
    }
  }
