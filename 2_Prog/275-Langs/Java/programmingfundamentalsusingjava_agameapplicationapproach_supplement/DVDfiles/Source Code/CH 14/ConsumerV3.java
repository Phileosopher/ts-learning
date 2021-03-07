  import java.util.Random;
  import java.util.concurrent.ArrayBlockingQueue; 

  public class ConsumerV3 implements Runnable
  {
    ArrayBlockingQueue <Integer> sharedData;
    int[] timesConsumed = new int[10];
    boolean[] consumedData = new boolean[10];

    public  ConsumerV3(ArrayBlockingQueue <Integer> sharedData) 
    {
      this.sharedData = sharedData;
    }

    public void run()
    { 
      Random delay = new Random();
      Integer dataItem = 0;

      for(int i = 1; i <= 10; i++)
      {
        try
        {
          Thread.sleep(delay.nextInt(10) + 1); //sumulate data fetch
          dataItem = (Integer) sharedData.take(); 
          System.out.println("Consumed " + dataItem + " <---"); 
        }
        catch(InterruptedException e)
        {
        }
            
        //record consumed statistics
        consumedData[dataItem - 1] = true;
        timesConsumed[dataItem - 1]++;
      }
      outputConsumedSummary();	
    }

    private void outputConsumedSummary()
    {
      try
      {
        Thread.sleep(5000);
      }
      catch(InterruptedException e)
      {
      }
      System.out.print("Consumed data: ");
      for(int i = 1; i <= 10; i++)
      {
        if(consumedData[i-1] == true)
        {
          System.out.print(" " + i); 
        }
      }  				
      System.out.print("\nTimes consumed:");
      for(int i = 1; i <= 10; i++)
      {
        if(consumedData[i-1] == true)
        {
          System.out.print(" " + timesConsumed[i-1]); 
        }
      }
    }
  }
