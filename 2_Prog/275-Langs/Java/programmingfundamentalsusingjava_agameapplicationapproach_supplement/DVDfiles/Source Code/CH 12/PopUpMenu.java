   import javax.swing.*;
 
   public class PopUpMenu
   {
     public static void main(String[] args)      
     {
       String title = "Pop Up Menus";
       PopUpMenuWindow window = new PopUpMenuWindow(title);
       window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		
       window.setVisible(true);
     }
   }
