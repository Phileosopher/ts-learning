  import javax.swing.*;

  public class PhoneBook 
  {   
    private String[] name; 
    private PhoneNumbers[] numbers; 
    
    public PhoneBook() 
    { 
      name = new String[3];
      numbers = new PhoneNumbers[3];

      for(int i = 0; i < name.length; i++)
      { 
        name[i] = JOptionPane.showInputDialog("enter your name");
        numbers[i] = new PhoneNumbers(i);
      }  
    }

    public void showAll()
    {
      for(int i = 0; i < name.length; i++)
      {
      System.out.println("\nName: " + name[i]);
      numbers[i].show();
      }
    }

    private class PhoneNumbers //an inner class 
    {
      private String home;
      private String cell;
      private String office;

      public PhoneNumbers(int i)
      {
        home = JOptionPane.showInputDialog("enter " + name[i] + 
                                           "'s HOME number");
        cell = JOptionPane.showInputDialog("enter " + name[i] +
                                           "'s CELL number");
        office = JOptionPane.showInputDialog("enter " + name[i] +
                                             "'s OFFICE number");
      }
      public void show()
      {   
        System.out.println("PhoneNumbers: home:" + home +
                           " cell:" + cell +  " office:" + office);
      }
    } //end of the inner class Phonenumbers
  }  
