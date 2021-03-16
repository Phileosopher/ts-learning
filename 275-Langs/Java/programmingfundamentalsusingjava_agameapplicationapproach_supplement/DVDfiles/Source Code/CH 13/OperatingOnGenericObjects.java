  public class OperatingOnGenericObjects 
  {   
    public static void main(String[] args) 
    {
      Integer[] iArray= {110, 36, 78, 43, 23, 83, 34, 24};
      StudentV2[] sArray = {new StudentV2(18, "Sam"),
                            new StudentV2(32, "Carol"),
                            new StudentV2(16, "Maggie"),
                            new StudentV2(25, "James")};

      System.out.println("iArray minimum is: " + min(iArray));
      System.out.println("sArray minimum is: " + min(sArray));
    }

    public static <T extends Comparable<T>> T  min(T[] anArray) 
    {
      T minimum = anArray[0];
      for(int i = 1; i < anArray.length; i++)
      {
        if(anArray[i].compareTo(minimum) < 0)
        {
          minimum = anArray[i];
        }
      }
      return minimum;
    }
  }     
