  import javax.swing.*; 
  import java.awt.*;
  import java.text.DecimalFormat;
  import java.awt.event.*;

  public class AddingMachineGUIV2 extends JFrame
  {
    JLabel description, plus, equals, sum, a, b;
    JTextField aValue, bValue;
    JButton compute, clear;

    public AddingMachineGUIV2(String title) 
    {
      super(title);      //Creates the window. All subsequent invocations 
      setSize(500, 250); //on an unnamed object operate on this window.
      setLocation(200, 100);
      setLayout(null);  
        
      //Step 1 declare the components
      description = new JLabel("Computes a + b");
      aValue = new JTextField();
      plus = new JLabel("+");
      bValue = new JTextField();
      equals = new JLabel("=");
      sum = new JLabel("x,xxx.xx"); 
      a = new JLabel("a");
      b = new JLabel("b");
      compute = new JButton("Compute");
      clear = new JButton("Clear");
        
      //Step 2: specify the component's properties
      description.setBounds(120, 0, 300, 30);
      description.setFont(new Font("Sherif", Font.BOLD, 24));
      aValue.setBounds(60, 50, 100, 30);
      plus.setBounds(190, 50, 20, 30);
      plus.setFont(new Font("Sherif", Font.BOLD, 20));
      bValue.setBounds(230, 50, 100, 30);
      equals.setBounds(350, 50, 20, 30);
      equals.setFont(new Font("Sherif", Font.BOLD, 20));
      sum.setBounds(380, 50, 100, 30);
      sum.setFont(new Font("Sherif", Font.BOLD, 20));
      a.setBounds(105, 75, 20, 30);
      a.setFont(new Font("Sherif", Font.BOLD, 20));
      b.setBounds(275, 75, 20, 30);
      b.setFont(new Font("Sherif", Font.BOLD, 20));
      compute.setBounds(65, 110, 90, 25);
      clear.setBounds(235, 110, 90, 25);
      clear.setToolTipText("Clears a, b and the sum");
    
      // Register the event handler methods
      compute.addActionListener(new ComputClickHandler());
      clear.addActionListener(new ClearClickHandler());
         		    
      //Step 4: add the component to the container
      add(description);
      add(aValue);
      add(plus);
      add(bValue);
      add(equals);
      add(sum);
      add(a);
      add(b);
      add(compute);
      add(clear);
    }
    //Event handler inner classes and methods
    public class ComputClickHandler implements ActionListener
    {
      public void actionPerformed(ActionEvent e)
      {   
        String s;
        double a, b, result;
        DecimalFormat f = new DecimalFormat("#,##0.00")

        s = aValue.getText();
        a = Double.parseDouble(s);
        s = bValue.getText();
        b = Double.parseDouble(s);
        result = a + b;
        sum.setText(f.format(result));
      }
    } 
    public class ClearClickHandler implements ActionListener
    {
      public void actionPerformed(ActionEvent e)
      {   
        aValue.setText("");
        bValue.setText("");
        sum.setText("x,xxx.xx");
      }
    }
  }
