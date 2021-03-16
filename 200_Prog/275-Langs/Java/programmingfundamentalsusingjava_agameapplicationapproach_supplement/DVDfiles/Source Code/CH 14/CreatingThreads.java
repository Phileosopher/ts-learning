  import java.util.concurrent.*;

  public class CreatingThreads 
  {
    public static void main(String[] args) 
    {
      // create a thread
      ExtendsThread thread1 = new ExtendsThread("thread1");
      
      // create a runnable object and then a thread
      ImplementsRunnable runnableObj1 = new ImplementsRunnable("thread2"); 
      Thread thread2 = new Thread(runnableObj1); //creates a thread1

      // create a runnable object and a thread pool
      ImplementsRunnable runnableObj2 = new ImplementsRunnable("thread3");
      ExecutorService threadLauncher = Executors.newCachedThreadPool();
    
      // initiate the threads
      thread1.start(); //initiates thread 1
      thread2.start(); //initiates thread 2

      // assign a runnable to a thread in the thread pool 
      threadLauncher.execute(runnableObj2);

      threadLauncher.shutdown();
    
      System.out.println("main method has completed its execution");
    }
  }
