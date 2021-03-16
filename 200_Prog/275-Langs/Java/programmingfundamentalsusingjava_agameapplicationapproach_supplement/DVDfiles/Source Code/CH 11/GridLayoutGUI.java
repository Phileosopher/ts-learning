  import javax.swing.*; 
  import java.awt.*;

  public class GridLayoutGUI extends JFrame
  {
    JButton first, second, third; 
    JLabel fourth; 
    JTextField fifth;

    public FlowLayoutGUI(String title) 
    {   
      super(title);
      setSize(650, 100);
      setLocation(200, 100);
      setLayout(new GridLayout(3, 2));
         
      //Step 1 declare the components
      first = new JButton("Added First"); 
      second = new JButton("Added Second"); 
      third = new JButton("Added Third"); 
      fourth = new JLabel("Added Fourth, too large"); 
      fifth = new JTextField("Added Fifth, a JTextField");
 
      //Step 2: specify the component's properties
      second.setFont(new Font("Sherif", Font.BOLD, 16));
      fourth.setFont(new Font("Sherif", Font.BOLD, 30));
      fifth.setFont(new Font("Sherif", Font.BOLD, 14));

      //Step 4:  add the components to the container
      add(first);
      add(second);
      add(third);
      add(fourth);
      add(fifth);
    }
  }
