// Programming Fundamentals Using MATLAB, Michael Weeks Copyright 2020
// 
public class HelloExample {
 
  public static int Count = 0; 

  public static void main(String[] args) { 
    Count = 3;
    System.out.println("HelloExample initialized");
  }

  public static void sayHello() { 
    Count++;
    if (Count > 2)
      Count = 0; 
    switch (Count) {
      case 0:
        System.out.println("Hello World!");
        break;
      case 1:
        System.out.println("Bonjour le Monde!");
        break;
      case 2:
        System.out.println("Hallo Welt!");
        break;
    }
  }
}

