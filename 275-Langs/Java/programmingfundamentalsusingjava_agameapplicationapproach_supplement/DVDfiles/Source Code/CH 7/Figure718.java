  Integer n1 = 20; 
  Integer n2 = 20; //a new object is not created, n2 is assigned n1
  if(n1 == n2) System.out.println("n1 and n2 refer to the same object");
  if(n1.equals(n2)) System.out.println("n1 & n2 contain the same value");

  n1 = 30;
  n2 = 30; //a new object is not created, n2 is assigned n1
  if(n1 == n2) System.out.println("n1 & n2 refer to the same object");
  if(n1.equals(n2)) System.out.println("n1 & n2 contain the same value");

  n2 = n1; //a new object is not created, n2 is assigned n1
  if(n1 == n2) System.out.println("n1 & n2 refer to the same object");;
  if(n1.equals(n2)) System.out.println("n1 & n2 contain the same value");

  n1 = 40;
  n2 = new Integer(40); //a new object is created
  if(n1 == n2) System.out.println("n1 & n2 refer to the same object");
  if(n1.equals(n2)) System.out.println("n1 & n2 contain the same value");
