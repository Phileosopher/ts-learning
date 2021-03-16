  import javax.swing.*;
  import java.awt.event.*;
  import java.awt.Color;
   
  public class PopUpMenuWindow extends JFrame implements ActionListener
  {
    JLabel aLabel = new JLabel("Right click this text to change its color");
   
    JPopupMenu aMenu = new JPopupMenu();
    JMenuItem blue = new JMenuItem("Blue");
    JMenuItem red = new JMenuItem("Red");
    JMenuItem green = new JMenuItem("Green");
 
    public PopUpMenuWindow(String title) 
    {
      super(title);
      setSize(400, 300);
      
      JPanel aPanel = new JPanel();
      aMenu.add(blue);
      aMenu.add(red);
      aMenu.add(green);
      
      blue.setMnemonic('B');
      red.setMnemonic('R');
      green.setMnemonic('G');

      blue.addActionListener(this);
      red.addActionListener(this);
      green.addActionListener(this);

      aLabel.setComponentPopupMenu(aMenu);
      aPanel.add(aLabel);
      add(aPanel);
    }

    public void actionPerformed(ActionEvent e)
    {
      if(e.getSource() == blue) aLabel.setForeground(Color.BLUE);
      if(e.getSource() == red) aLabel.setForeground(Color.RED);
      if(e.getSource() == green) aLabel.setForeground(Color.GREEN);
    }
  }
