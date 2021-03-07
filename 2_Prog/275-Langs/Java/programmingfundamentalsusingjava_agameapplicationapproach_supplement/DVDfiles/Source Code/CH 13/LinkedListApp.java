  public class LinkedListApp 
  {
    public static void main(String[] args) 
    {
      LinkedList <Transcripts> underGrads = new LinkedList<Transcripts>();
      Transcripts t1 = new Transcripts("Dana", 3.5, 45); 
      Transcripts t2 = new Transcripts("Carol", 3.8, 45); 
      Transcripts t3 = new Transcripts("Alice", 1.7, 22); 
      Transcripts t4 = new Transcripts("Bob", 2.6, 120); 
 
      underGrads.add(t1); //Add the transcripts to the list
      underGrads.add(t2);
      underGrads.add(t3);
      underGrads.add(t4);

      //Output the transcripts sequentially
      System.out.println("\nAll transcripts in order of entry");
      for(int i = 0; i < underGrads.size(); i++)
      {
        System.out.println(underGrads.get(i));
      }

      //The Collections class' sort method
      System.out.println("\nAll transcripts in sorted order by GPA");
      Collections.sort(underGrads);
      for(int i = 0; i < underGrads.size(); i++)
      {
         System.out.println(underGrads.get(i));
      }

      //The Collections class' min and max methods
      System.out.println("\nHighest GPA is " + 
                         Collections.max(underGrads));
      System.out.println("Lowest GPA is " + Collections.min(underGrads));

       //The Collection class' replaceAll method
       System.out.println("\nAll transcripts replacing "+
                          "Dana's transcript with Carol's transcript");
       Collections.replaceAll(underGrads, t1, t2);
       for(int i = 0; i < 4; i++)
       {
         System.out.println(underGrads.get(i));
       }

       //The Collections class' binarySearch method
       System.out.println("\nt4, Bob, is currently at location " + 
                          Collections.binarySearch(underGrads, t4));
                         
       //Use of an iterator
       System.out.println("\nAll transcripts output using an iterator " +
                            "after locations 0 and 3 were swapped");
       Collections.swap(underGrads,0, 3);
       ListIterator <Transcripts> anIterator = underGrads.listIterator(0);
       while (anIterator.hasNext())
       {
         System.out.println(anIterator.next());
       }
    }
  }
