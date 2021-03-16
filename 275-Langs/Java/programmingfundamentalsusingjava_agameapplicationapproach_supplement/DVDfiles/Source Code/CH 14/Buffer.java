  public class Buffer 
  {
    private int sharedData;

    public Buffer() 
    {

    }

    public void setData(int dataItem)
    {
      sharedData = dataItem;
    }

    public int getData()
    {
      return sharedData;
    }
  }
