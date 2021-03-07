  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;

  public class PCThreadSync 
  {
    public static void main(String[] args) 
    {
      SynchronizedBuffer aBuffer = new SynchronizedBuffer();
 
      ProducerV2 producerThread = new ProducerV2(aBuffer);
      ConsumerV2 consumerThread = new ConsumerV2(aBuffer);
       
      ExecutorService launcher = Executors.newCachedThreadPool();
      launcher.execute(producerThread);
      launcher.execute(consumerThread);

      launcher.shutdown();
    }
  }
