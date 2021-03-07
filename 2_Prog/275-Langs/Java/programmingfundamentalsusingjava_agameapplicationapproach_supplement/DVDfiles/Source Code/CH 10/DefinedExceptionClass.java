  import java.io.IOException;

  public class DefinedExceptionClass 
  {   
    public static void main(String[] args) 
    {   
      for(int i=1; i<=3; i++)
      {
       try
       {
         test(i);
       }
       catch(OffBoardException e) //a child of RuntimeException
       {
         System.out.print("Caught by the OffBoardException " +
                          "catch block: ");
         System.out.println(e.getMessage());
       }
       catch(RuntimeException e) //a child of Exception
       {
         System.out.print("Caught by the RuntimeException " + 
                          "catch block: ");
         System.out.println(e.getMessage());
       }
       catch(Exception e) //a child of throwable
       {
         System.out.print("Caught by the Exception catch block: ");
         System.out.println(e.getMessage());
       }
      }
    }
    public static void test(int path) throws Exception
    {
      if(path == 1) //throw an Exception object
      {
        throw new Exception("a message attached to an Exception object");
      }
      if(path == 2) //throw a RuntimeException object
      {
        throw new RuntimeException("a message attached to a " +
                                   "RuntimeException object");
      }
      if(path == 3) //throw an OffBoardException object
      {
        throw new OffBoardException("a message attached to an " +
                                    "OffBoardException object");
      }
    }
  }
