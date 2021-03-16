  public class StudentV4 implements Comparable <StudentV4>
  {
    private int id;
    private String name;

    public StudentV4(int id, String name) 
    { 
      this.id = id;
      this.name = name;
    }

    public String toString()
    {
      String s;
      return s = "ID: " + id + "; Name: " + name;
    }

    public int compareTo(StudentV4 s)
    {
      return name.compareTo(s.name);
    }
  }
