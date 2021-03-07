  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;
  import java.util.concurrent.ArrayBlockingQueue;

  public class PCThreadSyncAPI 
  {
    public static void main(String[] args) 
    {
      ArrayBlockingQueue <Integer> aBuffer;
      aBuffer = new ArrayBlockingQueue <Integer> (1);
      ProducerV3 producerThread = new ProducerV3(aBuffer);
      ConsumerV3 consumerThread = new ConsumerV3(aBuffer);
     
      ExecutorService launcher = Executors.newCachedThreadPool();
      launcher.execute(producerThread);
      launcher.execute(consumerThread);

      launcher.shutdown();
    }
  }
