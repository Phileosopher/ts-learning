  public class GenericClasses 
  {
    public static void main(String[] args) 
    { 
      Integer id = new Integer(1672);
      StudentV3 <String> s1 = new StudentV3 <String>("Sci103", "Tom");
      StudentV3 <Integer> s2 = new StudentV3 <Integer>(1672,"Maggie");
      StudentV3 <Integer> s3 = new StudentV3 <Integer>(45323, "Ryan"); 
      StudentV3 s4 = new StudentV3 <Integer>(53812, "Logan");
      StudentV3 <String> s5 = null;
      StudentV3 s6 = null; 

      System.out.println(s1);
      System.out.println(s2);
      System.out.println(s3);
      System.out.println(s4 + "\n");

      s5 = s1; //Safe
      s6 = s2; //Safe
      System.out.println(s5);
      System.out.println(s6);
    
      System.out.println(s5.compareTo(s6));
    }
  }
