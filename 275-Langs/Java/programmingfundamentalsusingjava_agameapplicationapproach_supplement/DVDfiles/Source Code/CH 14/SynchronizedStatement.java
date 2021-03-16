  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;

  public class SynchronizedStatement 
  {
    public static void main(String[] args) 
    {
      Counter shared = new Counter();
      AtmTransaction ATM1 = new AtmTransaction(shared);
      AtmTransaction ATM2 = new AtmTransaction(shared);

      ExecutorService launcher = Executors.newCachedThreadPool();

      launcher.execute(ATM1);
      launcher.execute(ATM2);

      launcher.shutdown();
    }
  }
