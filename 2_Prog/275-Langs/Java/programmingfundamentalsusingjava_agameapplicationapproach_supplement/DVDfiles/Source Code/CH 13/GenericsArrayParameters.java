  public class GenericsArrayParameters 
  {
    public static void main(String[] args) 
    {
      Integer[] intArray  = {10, 20, 30, 40, 50}; 
      Double[] doubleArray = {11.1, 22.2, 33.3, 44.4}; 
      Student[] studentArray = new Student[2];
      int intReturned;
      double doubleReturned;
      Student studentReturned;
        
      studentArray[0] = new Student(19, "Sam Jones");  
      studentArray[1] = new Student(20, "Nora King");
 
      intReturned = outputArray(intArray, 3); //AutoUnboxing the int
      doubleReturned = outputArray(doubleArray, 2); //AutoBoxing the real
      studentReturned = outputArray(studentArray, 1);
 
      System.out.println(intReturned);      
      System.out.println(doubleReturned);      
      System.out.println(studentReturned);      
    }
    
    public static <T> T outputArray(T[] anArray, int elementReturned)
    {
      for(int i = 0; i < anArray.length; i++)
      {
      System.out.println(anArray[i]);
      }
      System.out.println();
  
      return anArray[elementReturned];
    }
  }
