  public class Student 
  { private static int studentCount = 0;
    private int idNumber;
    private double gpa;
  
    public Student(int idNumber, double gpa)
    {
      studentCount++; //counts the number of Student objects declared
      this.idNumber = idNumber;
      this.gpa = gpa;
    }
    
    public String toString()
    { 
      String s = "id is " + idNumber +
                 "\ngpa is "  + gpa;
      return s;
    }

    public static int getStudentCount()
    { 
      return studentCount;
    }
  }
