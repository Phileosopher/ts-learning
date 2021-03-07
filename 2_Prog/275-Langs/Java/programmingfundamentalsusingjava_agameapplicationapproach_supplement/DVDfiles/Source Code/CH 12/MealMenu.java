  import javax.swing.*;
  import java.awt.event.*;

  public class MealMenu extends JFrame implements ActionListener
  {
    JPanel p1, p2;
    JRadioButton hamburger, taco, blt;
    JCheckBox cheese, ketchup, napkins;
    JButton placeOrder;

    public MealMenu() 
    {
      super("Dollar Meals");
      setLayout(null);
      setSize(303, 200);

      //Build the radio button entree panel		
      p1 = new JPanel(); //declare the panel
      p1.setLayout(null);
      p1.setBorder(BorderFactory.createTitledBorder("Entree"));
      p1.setBounds(5, 10, 140, 110); //locate and size the panel
        
      hamburger = new JRadioButton("Hamburger", true); //declare buttons
      taco = new JRadioButton("Taco");
      blt = new JRadioButton("BLT Sandwich");

      hamburger.setBounds(10, 20, 120, 20); //locate and size the buttons
      taco.setBounds(10, 50, 120, 20);
      blt.setBounds(10, 80, 120, 20);

      ButtonGroup bg1 = new ButtonGroup(); //group the buttons
      bg1.add(hamburger);
      bg1.add(taco);
      bg1.add(blt);

      p1.add(hamburger); //add the buttons to the panel
      p1.add(taco);
      p1.add(blt);
   
      //Build the check box extras panel   
      p2 = new JPanel(); //declare the panel
      p2.setLayout(null);
      p2.setBorder(BorderFactory.createTitledBorder("Extras"));
      p2.setBounds(150, 10, 140, 110); //locate and size the panel

      cheese = new JCheckBox("Cheese"); //declare the check boxes
      ketchup = new JCheckBox("Ketchup");
      napkins = new JCheckBox("Napkins");
    
      cheese.setBounds(10, 20, 120, 20); //locate and size the check boxes
      ketchup.setBounds(10, 50, 120, 20);
      napkins.setBounds(10, 80, 120, 20);

      p2.add(cheese); //add the check boxes to the panel
      p2.add(ketchup);
      p2.add(napkins);

      placeOrder = new JButton("Place Order"); //declare the JButton
      placeOrder.setBounds(80, 130, 120, 30); //locate and size it
      placeOrder.addActionListener(this); //register the event handler

      add(p1); //add the panels and the JButton to the content pane
      add(p2);
      add(placeOrder);
    }

    //Place order button handler
    public void actionPerformed(ActionEvent e)
    { 
      int extras = 0;
      String order = "";

      if(hamburger.isSelected() == true)
      {
        order = order + "Hamburger ";
      }
      else if(taco.isSelected() == true)
      {
        order = order + "Taco ";
      }
      else if(blt.isSelected() == true)
      {
        order = order + "BLT sandwich ";
      }
      if(cheese.isSelected() == true)
      {
        order = order + " and cheese";
        extras++;
      }
      if(ketchup.isSelected() == true)
      {
        order = order + " and ketchup";
        extras++;
      }
      if (napkins.isSelected() == true)
      {
        order = order + " and napkins";
        extras++;
      }
      if(extras == 0)
      {
        order = order + " no extras";
      }
      System.out.println(order);		
    }
  }
