    public static <T> T[] swap0and1(T[] anArray)
    { 
      T temp;

      temp = anArray[0];
      anArray[0] = anArray[1];
      anArray[1] = temp;

      return anArray;
    }
