  import java.util.*;
 
  public class Queues 
  {    
    public static void main(String[] args) 
    {
      ArrayDeque <WorkOrder> tasks = new ArrayDeque<WorkOrder>();
      PriorityQueue <WorkOrder> ptasks = new PriorityQueue<WorkOrder>();
    
      tasks.add(new WorkOrder("1C", "Polish door knob.", 10));
      tasks.add(new WorkOrder("8A", "Rats running around kitchen.", 1));
      tasks.add(new WorkOrder("8A", "Replace light bulb in hall.", 7));
      tasks.add(new WorkOrder("12B", "Toilet backing up.", 1));

      System.out.println("Work Orders Non-prioritized by an ArrayQueue");
      while(tasks.size() != 0)
      {
        System.out.println(tasks.remove());
      }

      System.out.println();
 
      ptasks.add(new WorkOrder("1C", "Polish door knob.", 10));
      ptasks.add(new WorkOrder("8A", "Rats running around kitchen.", 1));
      ptasks.add(new WorkOrder("8A", "Replace light bulb in hall.", 7));
      ptasks.add(new WorkOrder("12B", "Toilet backing up.", 1));

      System.out.println("Work Orders Prioritized by " +
                         "a PriorityQueue");
      while(ptasks.size() != 0)
      {
        System.out.println(ptasks.remove());
      }
    }
  }
