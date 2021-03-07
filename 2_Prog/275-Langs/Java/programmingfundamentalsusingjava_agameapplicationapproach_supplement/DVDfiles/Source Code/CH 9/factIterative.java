    public static long factIterative(int n)
    { 
      long nFact = 1;
      for(int i = n; i >= 1; i--)
      {
        nFact = nFact * i;
      }
      return nFact;  
    }
