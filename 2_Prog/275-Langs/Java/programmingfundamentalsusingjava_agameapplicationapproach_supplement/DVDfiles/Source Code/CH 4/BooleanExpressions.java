   public class BooleanExpressions 
   {   
      public static void main(String[] args) 
      {    
        int i1 = 5;
        double d1 = 3.53;   double d2 = 54.88; 
        char c1 = 'A';   char c2 ='C';
        boolean b1 = true;   boolean b2 = false;   
        String s1 = new String("Bob");
        String s2 = new String("Bob");

        System.out.println(i1 < 5); 
        System.out.println(d1 > d2);
         
        System.out.println(i1 >= d1); // integer i1 promoted
        System.out.println(d1 <= 3); // integer 3 is promoted
         
        System.out.println(c1 < c2); // lexicographical order used
        System.out.println(10 > c2); // c2 promoted to numeric 67
         
        System.out.println(b1 == b2) ;
     
        System.out.println( i1 == 5 || c1 < 'A' && d1 != 21.8 );
         
        System.out.println(s1 == s2); // compares contents of s1 and s2
      }
   }
