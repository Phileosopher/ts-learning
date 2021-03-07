  import javax.swing.*;
  import java.awt.event.*;

  public class ExpandedMealMenu extends JFrame implements ActionListener
  {
    JPanel p1, p2;
    String[] entreeItems = {"Hamburger", "Taco", "BLT Sandwich",
                            "Nachos", "Chicken Soup", "Hot Chile",
                            "Salad"};
    String[] extrasValues = {"Cheese", "Ketchup", "Napkins", "Mustard",
                             "Mayonnaise", "Salsa", "Paper Plate",
                             "Utensils", "Water"};
    JComboBox entree; 
    JList extrasList; 
    JButton placeOrder;

    public ExpandedMealMenu(String title) 
    {
      super(title);
      setLayout(null);
      setSize(303, 200);

      //Build the entree panel		
      p1 = new JPanel(); //declare the panel
      p1.setLayout(null);
      p1.setBorder(BorderFactory.createTitledBorder("Entree"));
      p1.setBounds(5, 10, 140, 110); //locate and size the entrée panel
        
      entree = new JComboBox(entreeItems);
      entree.setMaximumRowCount(4);
      entree.setBounds(10, 20, 120, 20);
      p1.add(entree);
   
      //Build extras panel   
      p2 = new JPanel(); //declare the panel
      p2.setLayout(null);
      p2.setBorder(BorderFactory.createTitledBorder("Extras"));
      p2.setBounds(150, 10, 140, 110); //locate and size the extras panel

      extrasList = new JList(extrasValues); 
      JScrollPane aScrollableList = new JScrollPane(extrasList); 
      aScrollableList.setBounds(10, 20, 120, 80); //80 displays 4 values
      p2.add(aScrollableList);

      placeOrder = new JButton("Place Order"); //declare the JButton
      placeOrder.setBounds(80, 130, 120, 30); //locate and size it
      placeOrder.addActionListener(this); //register its event handler

      add(p1); //add the panels and the JButton to the content pane
      add(p2);
      add(placeOrder);
    }

    //Place order button handler
    public void actionPerformed(ActionEvent e)
    { 
      Object[] extrasOrderedArray;

      System.out.print("\nEntree Number " + entree.getSelectedIndex() + 
                       ": " + entree.getSelectedItem() );

      extrasOrderedArray = extrasList.getSelectedValues();
      for(int i = 0; i < extrasOrderedArray.length; i++)
      { 
        System.out.print(", " + extrasOrderedArray[i]);
      }
    }
  }
