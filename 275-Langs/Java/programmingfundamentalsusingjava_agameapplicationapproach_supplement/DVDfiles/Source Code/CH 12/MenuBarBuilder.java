  import javax.swing.*;
  import java.awt.event.*;

  public class MenuBarBuilder extends JFrame 
  {
    //Menu item references
    private JMenuItem saladItem; 
    private JMenuItem chickenSoupItem;
    private JMenuItem bLTSubItem;
    private JMenuItem hamburgerSubItem;
    private JMenuItem tacoSubItem;
    private JMenuItem nachosSubItem;
    private JMenuItem chiliSubItem;
  
    public MenuBarBuilder(String title) 
    {
      super(title);
      setSize(303, 200);
      
      //Step 1: Create and add the menu bar to the JFrame
      JMenuBar menuBar = new JMenuBar();
      setJMenuBar(menuBar);

      //Step 2: Create and add the menus to the menu bar
      JMenu dropDownMenu = buildDollarMenu();
      menuBar.add(dropDownMenu);
    }
 
    //Step 3: Create and add the items and the submenus to the menu 
    public JMenu buildDollarMenu() //Builds and returns the dollar menu
    {
      // Create the drop down menu
      JMenu dollarMenu = new JMenu("Dollar");
      
      // Create the menu items and sub menus
      saladItem = new JMenuItem("Salad");
      chickenSoupItem = new JMenuItem("Chicken Soup");
      JMenu sandwichSubMenu = new JMenu("Sandwich");
      JMenu mexicanSubMenu = new JMenu("Mexican");

      // Add the menu items, submenus, and separators to the menu
      dollarMenu.add(saladItem);
      dollarMenu.add(chickenSoupItem);
      dollarMenu.addSeparator();
      dollarMenu.add(sandwichSubMenu);
      dollarMenu.addSeparator();
      dollarMenu.add(mexicanSubMenu);

      // Create submenu items
      bLTSubItem = new JMenuItem("BLT");
      hamburgerSubItem = new JMenuItem("Hamburger");
      tacoSubItem = new JMenuItem("Taco");
      nachosSubItem = new JMenuItem("Nachos");
      chiliSubItem = new JMenuItem("Chili");

      // Add the submenu items to the submenus 
      sandwichSubMenu.add(hamburgerSubItem);
      sandwichSubMenu.add(bLTSubItem);
      mexicanSubMenu.add(tacoSubItem);
      mexicanSubMenu.add(nachosSubItem);
      mexicanSubMenu.add(chiliSubItem);

      //Assign mnemonics to the menu items
      saladItem.setMnemonic('S');
      chickenSoupItem.setMnemonic('C');
      bLTSubItem.setMnemonic('B');
      hamburgerSubItem.setMnemonic('H');
      tacoSubItem.setMnemonic('T');
      nachosSubItem.setMnemonic('N');
      chiliSubItem.setMnemonic('L');
    
      // Register event handlers
      saladItem.addActionListener(new dollarMenuListener());
      chickenSoupItem.addActionListener(new dollarMenuListener());
      bLTSubItem.addActionListener(new dollarMenuListener());
      hamburgerSubItem.addActionListener(new dollarMenuListener());
      tacoSubItem.addActionListener(new dollarMenuListener());
      nachosSubItem.addActionListener(new dollarMenuListener());
      chiliSubItem.addActionListener(new dollarMenuListener());
 
      return dollarMenu;
    }   

    public class dollarMenuListener implements ActionListener
    {
      public void actionPerformed(ActionEvent e)
      { 
        String entree = "";     	
      
        if(e.getSource() == saladItem) entree = "Salad";
        if(e.getSource() == chickenSoupItem) entree = "Chicken Soup";
        if(e.getSource() == bLTSubItem) entree = "BLT Sandwich";
        if(e.getSource() == hamburgerSubItem) entree = "Hamburger";
        if(e.getSource() == tacoSubItem) entree = "Taco";
        if(e.getSource() == nachosSubItem) entree = "Nachos";
        if(e.getSource() == chiliSubItem) entree = "Chili";
        System.out.println("Dollar Meal Entree: " + entree);
      }
    }  
  }
