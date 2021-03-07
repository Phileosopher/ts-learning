  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;

  public class PCThreadProblems 
  {
    public static void main(String[] args) 
    {
      Buffer aBuffer = new Buffer();
 
      Producer producerThread = new Producer(aBuffer);
      Consumer consumerThread = new Consumer(aBuffer);
       
      ExecutorService launcher = Executors.newCachedThreadPool();
      launcher.execute(producerThread);
      launcher.execute(consumerThread);

      launcher.shutdown();
    }
  }
