       public class AVoidMethod 
       {   
          public static void main(String[] args) 
          {
             AVoidMethod.outputNewspaperName(); //1st method invocation
             System.out.println("Page 1\n");
             outputNewspaperName();             //2nd method invocation
             System.out.println("Page 2\n");    
          }
    
         static void outputNewspaperName()     //method signature
         {
            System.out.println("The Student Voice");
         }
       }
