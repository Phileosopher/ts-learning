
  public JMenu buildExtrasMenu() //Builds and returns the extras menu
  {
    //Create the menu object
    JMenu extrasMenu = new JMenu("Extras");
   
    //Create the menu items and sub menus
    cheeseItem = new JCheckBoxMenuItem("Cheese");
    waterItem = new JCheckBoxMenuItem("Water");
    paperPlateItem = new JCheckBoxMenuItem("Paper plate");
    utensilItem = new JCheckBoxMenuItem("Utensils");
    mustardItem = new JRadioButtonMenuItem("Mustard");
    mayonnaiseItem = new JRadioButtonMenuItem("Mayonnaise");
    katchupItem = new JRadioButtonMenuItem("Katchup"); 
    salsaItem = new JRadioButtonMenuItem("Salsa");
 
    //Create button group
    ButtonGroup bg = new ButtonGroup();
    bg.add(mustardItem);
    bg.add(mayonnaiseItem);
    bg.add(katchupItem);
    bg.add(salsaItem);

    //Add the menu items to the menu
    extrasMenu.add(cheeseItem);
    extrasMenu.add(waterItem);
    extrasMenu.add(paperPlateItem);
    extrasMenu.add(utensilItem);
    extrasMenu.addSeparator();
    extrasMenu.add(mustardItem);
    extrasMenu.add(mayonnaiseItem);
    extrasMenu.add(katchupItem);
    extrasMenu.add(salsaItem);
     
    //Register event handlers
    cheeseItem.addActionListener(new ExtrasMenuListener());
    waterItem.addActionListener(new ExtrasMenuListener());
    paperPlateItem.addActionListener(new ExtrasMenuListener());
    utensilItem.addActionListener(new ExtrasMenuListener());
    mustardItem.addActionListener(new ExtrasMenuListener());
    mayonnaiseItem.addActionListener(new ExtrasMenuListener());
    katchupItem.addActionListener(new ExtrasMenuListener());
    salsaItem.addActionListener(new ExtrasMenuListener());
 
    return extrasMenu;
  }
  
