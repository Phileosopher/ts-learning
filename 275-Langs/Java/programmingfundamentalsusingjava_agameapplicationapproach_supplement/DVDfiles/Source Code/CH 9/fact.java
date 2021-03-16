   public long fact(int n)
   { 
     long nMinus1Factorial, nFact;
     if(n == 0) //return the definition of 0! (the base case)
     {
       return 1;
     }
     else //calculate (n-1)! and then n!
     {
      nMinus1Factorial = fact(n-1); //fact invokes itself on this line
      nFact = n * nMinus1Factorial;
      return nFact;  
    }
  }
