  public class GenericOverloading 
  {
    public static void main(String[] args) 
    {
      IdentifyYourself(1, 2); //int, int: Version 1
      IdentifyYourself(new Integer(10), 2); //object, int: Version 2
      IdentifyYourself(2, new Double(20.3)); //int, object: Version 3a
      IdentifyYourself(new Integer(10), new Student(19, "Evie")); //V3a
    }

    // Version 3a
    public static <T1, T2> void IdentifyYourself(T1 a, T2 b)
    {
      System.out.println("Version 3a was invoked");
    }

    // Version 2
    public static <T> void IdentifyYourself(T a, int b) 
    {
      System.out.println("Version 2 was invoked");
    }

    // Version 1
    public static void IdentifyYourself(int a, int b) 
    {
      System.out.println("Version 1 was invoked");
    }
  }


