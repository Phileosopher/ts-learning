  // A Non-Generic Queue. It can only queue SuudentV4 Objects

  public class Queue
  {  
    private int size;
    private int numOfNodes = 0;
    private int front = 0;
    private int rear = 0;
    private StudentV4[] data;   

    public Queue(int n)
    {  
      size = n;
      data = new StudentV4[n];
    }

    public boolean enQueue(StudentV4 newItem) //add a StudentV4 object
    {  
      if(numOfNodes == size) //The queue is full
      {
        return false;  
      }
      else //add the object to the structure
      {
        numOfNodes = numOfNodes + 1;
        data[rear] = newItem;
        rear = (rear + 1) % size;
        return true;  
      }
    }

    public StudentV4 deQueue( ) //fetch and delete a StudentV4 object
    {  
      int frontLocation;
      if(numOfNodes == 0) //The queue is empty
      {
        return null;  
      }
      else //return an object from the structure
      {
        frontLocation = front;
        front = (front + 1) % size;
        numOfNodes = numOfNodes - 1;
        return data[frontLocation];
      }
    }
  }
