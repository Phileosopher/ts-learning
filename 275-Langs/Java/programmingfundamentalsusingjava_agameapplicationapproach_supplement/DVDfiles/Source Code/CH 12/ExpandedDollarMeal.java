   import javax.swing.*;
 
   public class ExpandedDollarMeal 
   {
     public static void main(String[] args) 
     {
       String title = "Expanded Dollar Meal";
       ExpandedMealMenu window = new ExpandedMealMenu(title);
       window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		
       window.setVisible(true);
     }
   }
