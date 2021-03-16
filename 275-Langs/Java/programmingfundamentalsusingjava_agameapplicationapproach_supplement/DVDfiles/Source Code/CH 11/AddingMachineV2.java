  import javax.swing.*;
  import java.awt.*;

  public class AddingMachineV2 
  {    
    public static void main(String[] args) 
    {
      AddingMachineGUIV2 calculator = new AddingMachineGUIV2("Calculator");
      calculator.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      calculator.setVisible(true);
    }
  }
