  import java.util.ArrayList;

  public class GenericQueue <T> 
  {  
    private int size;
    private int numOfNodes = 0;
    private int front = 0;
    private int rear = 0;
    private ArrayList <T> data;      

    public GenericQueue(int n)
    {  
      size = n;
      data = new ArrayList <T> (size);     
    }

    public boolean enQueue(T newItem)
    {   
      if(numOfNodes == size) //The queue is full
      {
        return false;  
      }
      else // add the object to the structure
      { 
        numOfNodes = numOfNodes + 1;
        data.add(rear, newItem);  //data[rear] = (T) item.clone();
        rear = (rear + 1) % size;
        return true;  
      }
    }

    public T deQueue( ) //fetch and delete an object
    {  
      int frontLocation;
      if(numOfNodes == 0) //The queue is empty
      {
        return null; 
      }
      else 
      { 
        frontLocation = front;
        front = (front + 1) % size;
        numOfNodes = numOfNodes - 1;
        return data.get(frontLocation); 
      }
    }
  }
