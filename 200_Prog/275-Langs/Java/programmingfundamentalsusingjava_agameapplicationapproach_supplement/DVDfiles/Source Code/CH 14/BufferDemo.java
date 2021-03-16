  public class BufferDemo 
  {
    public static void main(String[] args) 
    {
      private Buffer aBuffer = new Buffer();
      private int dataItem;
    
      for(int i = 1; i <= 3; i++)
      {
        aBuffer.setData(i); //produce a data item
        System.out.println("Produced " + i);
    
        dataItem = aBuffer.getData(); //consume a data item
        System.out.println("Consumed " + dataItem);  
      }
    }
  }
