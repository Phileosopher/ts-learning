  import java.util.Arrays;

  public class ReturningGenericArrays 
  {
    public static void main(String[] args) 
    {
      Integer[] iArray= {1,2,3,4};
      Integer[] iArrayReturned;
      Student[] sArray = {new Student(17, "Robert"),
                          new Student(20, "Carol"),
                          new Student(16, "Maggie")};
      Student[] sArrayReturned;

      iArrayReturned = invertArray(iArray);
      sArrayReturned = invertArray(sArray);

      for(int i = 0; i < iArray.length; i++) //all the Integer Objects
      {
        System.out.println(iArray[i] + "\t" + iArrayReturned[i]);
      }
      System.out.println();
 
      for(int i = 0; i < sArray.length; i++) //all the Student Objects
      {
        System.out.println(sArray[i] + "\t" + sArrayReturned[i]);
      }
    }

    public static <T1> T1[] invertArray(T1[] anArray) 
    {
      T1[] copy;

      copy = Arrays.copyOf(anArray, anArray.length);
      for(int i = 0; i < copy.length; i++)
      {
        copy[i] = anArray[copy.length – 1 - i];
      }
      return copy;
    }
  }
