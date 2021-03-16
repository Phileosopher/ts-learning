   import javax.swing.*;
 
   public class Menus
   {
     public static void main(String[] args) 
     {
       String title = "Expanded Dollar Meal Menu";
       MenuBarBuilder window = new MenuBarBuilder(title);
       window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		
       window.setVisible(true);
     }
   }
