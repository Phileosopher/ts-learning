    import java.text.DecimalFormat;

    public class DecimalFormatClass 
    {  
       public static void main(String[] args) 
       {
          DecimalFormat cs = new DecimalFormat("#,###.###"); //commas    	
          DecimalFormat ltz = new DecimalFormat("#,##0.000"); //zeros    	
          DecimalFormat pct = new DecimalFormat("#,##0.00%"); //percentages   
          DecimalFormat sn = new DecimalFormat("0.0000E0"); //scientific   
          double n1 = 0.0062;
          double n2 = 161234563468.5;
  	  double n3 = 1.530;

  	  System.out.println("Comma-separators");
  	  System.out.println(cs.format(n1));
  	  System.out.println(cs.format(n2));
  	  System.out.println(cs.format(n3));
  	
 	  System.out.println("\nLeading & Trailing Zeros, & Commas");
  	  System.out.println(ltz.format(n1));
  	  System.out.println(ltz.format(n2));
  	  System.out.println(ltz.format(n3));
 	
  	  System.out.println("\nPercentages");
  	  System.out.println(pct.format(n1));
  	  System.out.println(pct.format(n2));
  	  System.out.println(pct.format(n3));

  	  System.out.println("\nScientific Notation");
 	  System.out.println(sn.format(n1));
  	  System.out.println(sn.format(n2));
  	  System.out.println(sn.format(n3));
      }
    }
