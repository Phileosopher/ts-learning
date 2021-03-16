  public class TowersOfHanoi 
  {
    public static void main(String[] args) 
    {
      hanoi(4, "A", "B", "C"); //output the solution fro four rings
    }
    
    public static void hanoi(int nRings, String fromTower, String toTower,
                             String thirdTower)
    {
        
      if(nRings == 1) //base case
      {
        System.out.println("move one ring from tower " + fromTower +
                           " to tower " + toTower); 
        return;
      }

      //general solution
      hanoi(nRings-1, fromTower, thirdTower, toTower); //reduced problem
      System.out.println("move one ring from tower " + fromTower +
                         " to tower " + toTower);
      hanoi(nRings-1, thirdTower, toTower, fromTower); //reduced problem
    }
  }
