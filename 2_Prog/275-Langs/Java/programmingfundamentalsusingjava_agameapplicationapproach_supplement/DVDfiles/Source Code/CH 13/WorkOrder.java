  public class WorkOrder implements Comparable <WorkOrder>
  {
    String apartmentNumber;
    String description;
    int priority;	
    
    public WorkOrder(String location, String description, int priority)
    {
      apartmentNumber = location;
      this.description = description;
      this.priority = priority;
    }
    
    public String toString()
    {
      return "Apartment " + apartmentNumber +
             ", " + description;
    }
   
    public int compareTo(WorkOrder aWorkOrder)
    {
      return priority - aWorkOrder.priority;
    }
  }
