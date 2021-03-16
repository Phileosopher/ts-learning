  import javax.swing.*; 
  import java.awt.*;
   
  public class AddingMachineGUI3 extends JFrame
  {
    JLabel description, a, plus, b, equals, sum, centerSpace;
    JTextField aValue, bValue;
    JButton compute, clear;
    JPanel panel1 = new JPanel();
    JPanel panel2 = new JPanel();
    JPanel panel3 = new JPanel();

    public AddingMachineGUI3(String title) 
    {   
      super(title);
      setSize(475, 150);
      setLocation(200, 100);
      setLayout(new BorderLayout());
   
      //Declaration of the atomic components
      description = new JLabel("Computes a + b"); 
      a = new JLabel("a");
      aValue = new JTextField(5);
      plus = new JLabel("   +    ");
      b = new JLabel("b");
      bValue = new JTextField(5);
      equals = new JLabel("   =   ");
      sum = new JLabel("x,xxx.xx"); 
      compute = new JButton("Compute");
      centerSpace = new JLabel("     ");
      clear = new JButton("    Clear    ");
     
      //Specify the component's properties
      description.setFont(new Font("Sherif", Font.BOLD, 24));
      plus.setFont(new Font("Sherif", Font.BOLD, 20));
      equals.setFont(new Font("Sherif", Font.BOLD, 20));
      sum.setFont(new Font("Sherif", Font.BOLD, 20));
      a.setFont(new Font("Sherif", Font.BOLD, 20));
      b.setFont(new Font("Sherif", Font.BOLD, 20));
      clear.setToolTipText("Clears a, b and the sum");
     
      //Step 4: add the components to the window or non-atomic container
      panel1.add(description);
      panel2.add(a);
      panel2.add(aValue);
      panel2.add(plus);
      panel2.add(b);
      panel2.add(bValue);
      panel2.add(equals);
      panel2.add(sum);
      panel3.add(compute);
      panel3.add(centerSpace);
      panel3.add(clear);
      add(panel1, BorderLayout.NORTH);
      add(panel2, BorderLayout.CENTER);
      add(panel3, BorderLayout.SOUTH);
    }
  }
