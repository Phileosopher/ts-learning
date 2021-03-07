  public class StudentV2 implements Comparable<StudentV2>
  {
    private int age;
    private String name;
 
    public StudentV2(int age, String name) 
    {
      this.age = age;
      this.name = name;
    }

    public String toString()
    {
      String s;
      return s = "age " + age + " name " + name;
    }

    public int compareTo(StudentV2 s1)
    {
      return age - s1.age;
    }
  }
