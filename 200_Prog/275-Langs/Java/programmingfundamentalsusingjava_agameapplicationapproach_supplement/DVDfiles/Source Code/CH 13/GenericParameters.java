  public class GenericParameters 
  {
    public static void main(String[] args) 
    {
      int amount = 45;
      double price = 567.89;
      char initial = 'P';
      Student s1 = new Student(19, "Sam Jones");
      double returnedPrice;
      Student returnedStudent;

      returnedPrice = output2Objects(amount, price);
      returnedStudent = output2Objects(initial, s1);
      System.out.println(returnedPrice);
      System.out.println(returnedStudent);
    }           
    
    public static <T1, T2> T2 output2Objects(T1 object1, T2 object2)
    {
      System.out.println(object1);
      System.out.println(object2 + "\n");
 
	  return object2;
    }
  } 
