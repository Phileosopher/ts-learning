  import javax.swing.*;
  import java.awt.*;

  public class AddingMachine 
  {    
    public static void main(String[] args) 
    {
      AddingMachineGUI calculator = new AddingMachineGUI("Calculator");
      calculator.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      calculator.setVisible(true);
    }
  }
