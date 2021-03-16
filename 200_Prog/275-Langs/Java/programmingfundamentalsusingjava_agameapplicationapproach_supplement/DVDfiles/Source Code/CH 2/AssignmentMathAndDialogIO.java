      import javax.swing.JOptionPane;
    
      public class AssignmentMathAndDialogIO 
      {
         public static void main(String[] args) 
         {
            String s;
            double area, radius;
        
            JOptionPane.showMessageDialog(null, "Circle area and radius" + 
                                              "\n calculation program");
            s = JOptionPane.showInputDialog("To calculate an area," +
                                          "\n     enter a radius"); 
            radius = Double.parseDouble(s);
            area = Math.PI * Math.pow(radius, 2);
            JOptionPane.showMessageDialog(null, "The area of a circle" +
                                                " whose radius = " +
                                                radius + "\nis " + area);     
        
            s =JOptionPane.showInputDialog("To calculate a radius" +
                                          "\n    enter an area"); 
            area = Double.parseDouble(s);
            radius = Math.sqrt(area / Math.PI); 
            JOptionPane.showMessageDialog(null, "The radius of a circle" +
                                               " whose area = " +
                                                area + "\nis " + radius);     
          }
       }
