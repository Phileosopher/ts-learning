  public class Patient 
  {
    String name;
    String DOB;
    String cellNumber;

    public Patient(String name, String DOB, String cellNumber) 
    {
      this.name = name;
      this.DOB = DOB;
      this.cellNumber = cellNumber;
    }
    public String toString()
    {
      return name + ", \tDOB: " + DOB + ", \tCell Number: " + cellNumber;
    }
  }
