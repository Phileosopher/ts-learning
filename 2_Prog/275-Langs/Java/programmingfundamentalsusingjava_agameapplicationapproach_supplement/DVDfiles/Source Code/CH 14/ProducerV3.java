  import java.util.Random;
  import java.util.concurrent.ArrayBlockingQueue; 

  public class ProducerV3 implements Runnable
  {
    ArrayBlockingQueue <Integer> sharedData;
    Random delay = new Random();

    public ProducerV3(ArrayBlockingQueue <Integer> sharedData) 
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
          sharedData.put(i); 
          System.out.println("Produced " + i); 
        }
        catch(InterruptedException e)
        {
        }
      }
    }
  }
