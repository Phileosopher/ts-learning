  public class AtmTransaction implements Runnable
  {
    private Counter shared;

    public AtmTransaction(Counter shared) 
    {
      this.shared = shared;
    }

    public void run()
    {   
      int count;

      while(true) 
      {   
        try
        { 
          synchronized(shared) //incrementing of the transaction counter
          { 
            if(shared.getCount() >= 3) //reached transaction limit
            {
              break;
            }
            count = shared.getCounter();
            Thread.sleep(10); //simulate end of time quantum
            shared.setCounter(count + 1);
            Counter.outputCounter();	
          }
        }
        catch(InterruptedException e)
        {
        }
          //code to process a deposit
      }
      System.out.println("An ATM is shutting down"); 
    }
  }
