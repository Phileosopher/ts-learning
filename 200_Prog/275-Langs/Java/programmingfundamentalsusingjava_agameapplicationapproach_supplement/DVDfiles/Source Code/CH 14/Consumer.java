  import java.util.Random;

  public class Consumer implements Runnable
  {
    private Buffer sharedData;
    private int[] timesConsumed = new int[10];
    private boolean[] consumedData = new boolean[10];

    public Consumer(Buffer sharedData) 
    {
      this.sharedData = sharedData;
    }

    public void run()
    { 
      Random delay = new Random();
      int dataItem;

      for(int i = 1; i <= 10; i++)
      {
        try
        {
          Thread.sleep(delay.nextInt(10) + 1); //simulate data fetch
        }
        catch(InterruptedException e)
        {
        }
        dataItem = sharedData.getData();
        System.out.println("Consumed " + dataItem + " <---");
            
        //record consumed statistics
        consumedData[dataItem - 1] = true;
        timesConsumed[dataItem - 1]++;
      }
      outputConsumedSummary();	
    }

    private void outputConsumedSummary()//outputs final statistics
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
