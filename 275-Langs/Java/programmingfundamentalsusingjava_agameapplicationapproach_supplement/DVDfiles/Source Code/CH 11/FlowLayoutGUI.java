   import javax.swing.*; 
   import java.awt.*;

   public class FlowLayoutGUI extends JFrame
   {
     JButton first, second, third; 
     JLabel fourth; 
     JTextField fifth;

    public FlowLayoutGUI(String title) 
    {   
      super(title);
      setSize(650, 180);
      setLocation(200, 100);
      setLayout(new FlowLayout()); //Override the default BorderLayout
 
      //Step 1 declare the components
      first = new JButton("Added First"); 
      second = new JButton("Added Second, Large Font Sets Row's Height");
      third = new JButton("Added Third, Could Not Fit on Row 1"); 
      fourth = new JLabel("Added Fourth, Component's Width Forces " +
                          "Fifth Component to the Next Row"); 
      fifth = new JTextField("Added Fifth, Components are Centered " +
                             "in the Rows");
 
      //Step 2: specify the component's properties
      second.setFont(new Font("Sherif", Font.BOLD, 22));
      fourth.setFont(new Font("Sherif", Font.BOLD, 16));
      fifth.setFont(new Font("Sherif", Font.BOLD, 14));

      //Step 4: add the components to the container (Step 3 is skipped)
      add(first);
      add(second);
      add(third);
      add(fourth);
      add(fifth);
    }
  }
