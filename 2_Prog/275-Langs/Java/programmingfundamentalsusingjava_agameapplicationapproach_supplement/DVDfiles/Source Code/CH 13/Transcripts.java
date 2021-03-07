  public class Transcripts implements Comparable <Transcripts>
  {
    String name;
    double gpa;
    int creditsEarned;

    public Transcripts(String name, double gpa, int creditsEarned)
    {
      this.name = name;
      this.gpa = gpa;
      this.creditsEarned = creditsEarned;	
    }

    public String toString()
    {
      return "name: " + name +
             "; gpa: " + gpa +
             "; credits earned: " + creditsEarned;
    }
    
    public int compareTo(Transcripts aTranscript)
    { 
        //Defines the natural order of transcripts
      int gpa1 = (int) (gpa * 100); 
      int gpa2 = (int) (aTranscript.gpa * 100); 
      return gpa1 - gpa2;
    }
  }
