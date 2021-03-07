  import java.util.Random;

  public class ProducerV2 implements Runnable
  {
    private SynchronizedBuffer sharedData;
    private Random delay = new Random();

    public ProducerV2(SynchronizedBuffer sharedData) 
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
