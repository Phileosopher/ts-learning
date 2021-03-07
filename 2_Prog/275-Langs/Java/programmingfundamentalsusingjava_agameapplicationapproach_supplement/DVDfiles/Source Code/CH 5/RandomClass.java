   import java.util.Random;
   import javax.swing.*;
 
   public class RandomClass 
   {
     public static void main(String[] args) 
     {
       Random randomObject = new Random(); //time of day seed value
       int min = 32;
      int max = 38;
      int secretNumber;
      String sGuess;
      int count = 1;
    	
      secretNumber = min + randomObject.nextInt(max - min + 1);
      JOptionPane.showMessageDialog(null, "Secret Number Guessing Game" +
                                          "\nguess a number between " +
                                            max + " and " + min);
      do
      {
        sGuess = JOptionPane.showInputDialog("Enter a guess " + count + 
                                           "\nOr click Cancel to quit");
        count++;
        if(sGuess == null) //Cancel was clicked
        {
          break;
        }
      }while(secretNumber != Integer.parseInt(sGuess));
    	
      if(sGuess == null) //Cancel was clicked
      {
        JOptionPane.showMessageDialog(null, "Secret Number was " +
                                             secretNumber);
      }
      else
      {
   	  JOptionPane.showMessageDialog(null, "Great, you guessed it.");	
      }
    }
  }
