       import java.text.DecimalFormat;
      
       public class BasicNumericFormatting
       {
         public static void main(String[] args)
         {    
           double speedOfLight = 299792458.7153;
           int population = 1097603176;
    
           DecimalFormat df = new DecimalFormat("#,###.##");
    
           System.out.println(df.format(speedOfLight));
           System.out.println(df.format(population));
         }
       }
