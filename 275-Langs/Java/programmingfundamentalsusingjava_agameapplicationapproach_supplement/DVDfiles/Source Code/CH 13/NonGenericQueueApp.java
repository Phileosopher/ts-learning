  public class NonGenericQueueApp
  {
    public static void main(String[] args) 
    {
      Queue aQueue = new Queue (4);
      StudentV4 aStudent;

      aStudent = new StudentV4(1, "Nora");
      aQueue.enQueue(aStudent);
      aStudent = new StudentV4(2, "Logan");
      aQueue.enQueue(aStudent);
      aStudent = new StudentV4(3, "Evie");
      aQueue.enQueue(aStudent);
      aStudent = new StudentV4(4, "Ryan");
      aQueue.enQueue(aStudent);
      aStudent = new StudentV4(5, "Skyler"); //Queue already full
      System.out.println("Fifth enqueue successful? " + 
                          aQueue.enQueue(aStudent));
    
      for(int i=1; i <= 5; i++) //one more than the queue's capacity
      {
        System.out.println(aQueue.deQueue());
      }
    }
  }
