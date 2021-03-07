  public class StudentV3 <T> implements Comparable<StudentV3>  
  {
    private T id;
    private String name;

    public StudentV3(T id, String name) 
    { 
      this.id = id;
      this.name = name;
    }
    public String toString()
    {
      String s;
      return s = "ID: " + id + "; Name: " + name;
    }
    public int compareTo(StudentV3 s)
    {
      return name.compareTo(s.name);
    }
  }
