   import java.util.Arrays;
   public class ArraysClass 
   {    
     public static void main(String[] args) 
     {
       String[] stringArray = {"Tom","Mary","Bob","Alice","Joe","Fred"};
       String[] copyStringArray;
       int[] intArray = { 3, 5, 2, 8, 6, 4};
       int[] copyIntArray;
      int[] filledIntArray;

      //outputting the elements of an arrays
      System.out.println("Outputing arrays using the " +
                         "Arrays.toString method");
      System.out.println(Arrays.toString(stringArray));
      System.out.println(Arrays.toString(intArray));

      //copying the elements of an array;
      System.out.println("\nCopying arrays using the " + 
                         "Arrays.copyOf method");
      copyStringArray = Arrays.copyOf(stringArray, 10);
      System.out.println(Arrays.toString(copyStringArray));
      copyIntArray = Arrays.copyOf(intArray, intArray.length);
      System.out.println(Arrays.toString(copyIntArray));

      //determining if all the elements of two arrays are equal
      System.out.println("\nTesting two arrays for equality " + 
                         "using the Arrays.equals method");
      System.out.println(Arrays.equals(intArray, copyIntArray));
      copyIntArray[0] = 1;    	
      System.out.println(Arrays.equals(intArray, copyIntArray));

      //sorting arrays
      System.out.println("\nSorting all or part of an array: " + 
                         "the Arrays.sort method");
      Arrays.sort(stringArray);
      System.out.println(Arrays.toString(stringArray));
      Arrays.sort(intArray, 1, 5);
      System.out.println(Arrays.toString(intArray));

      //searching for an element of a sorted array
      System.out.println("\nSearching for a value: the " + 
                         "Arrays.binarySearch method");
      System.out.println(Arrays.binarySearch(stringArray, "Fred"));
      System.out.println(Arrays.binarySearch(stringArray, "Doris"));

      //copying a part of an array
      System.out.println("\nPartial copies: the " +
                         "Arrays.copy and copyRange methods");
      copyIntArray = Arrays.copyOf(intArray, 4);
      System.out.println(Arrays.toString(copyIntArray));
      copyIntArray = Arrays.copyOfRange(intArray, 2, 10);
      System.out.println(Arrays.toString(copyIntArray));

      //setting all elements of a array to one value
      System.out.println("\nFilling all or part of an array: " +
                         "the Arrays.fill method");
      Arrays.fill(intArray, 4);
      System.out.println(Arrays.toString(intArray));
      Arrays.fill(stringArray, 1, 4, "FillValue");
      System.out.println(Arrays.toString(stringArray));
    }
  }
