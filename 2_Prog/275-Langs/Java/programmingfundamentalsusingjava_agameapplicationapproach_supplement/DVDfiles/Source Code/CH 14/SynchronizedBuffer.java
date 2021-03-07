  public class SynchronizedBuffer
  {
    int sharedData;
    private boolean writeable = true;
    private boolean readable = false;

    public SynchronizedBuffer() 
    {

    }

    public synchronized void setData(int dataItem)
    { 
      try
      {
        while(writeable == false)
        {
          wait();
        }
      }
      catch(InterruptedException e)
      {
      }

      sharedData = dataItem;
      writeable = false;
      readable = true;
      notifyAll();
    }

    public synchronized int getData()
    { 
      private int dataItem;
      try
      {
        while(readable == false)
        {
          wait();
        }
      }
      catch(InterruptedException e)
      {
      }

      writeable = true;
      readable = false;
      dataItem = sharedData;
      notifyAll();
      return dataItem;
    }
  }
