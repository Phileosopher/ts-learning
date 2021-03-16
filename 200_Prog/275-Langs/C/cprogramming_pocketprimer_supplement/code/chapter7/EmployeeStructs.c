#include <stdio.h>
#include <string.h>

typedef struct Employee
{
   char  fname [50];
   char  lname [50];
   char  title [100];
   int   emp_id;
} emp;

int main()
{
   struct Employee emp1;

   strcpy( emp1.fname, "John");
   strcpy( emp1.lname, "Smith");
   strcpy( emp1.title, "Developer");
   emp1.emp_id = 2000;

   printf("First name:  %s\n",emp1.fname);
   printf("Last name:   %s\n",emp1.lname);
   printf("Title:       %s\n",emp1.title);
   printf("Employee id: %d\n",emp1.emp_id);

   struct Employee *empptr = &emp1;
   printf("\nPointer of Employee:\n");
   printf("First name:  %s\n",empptr->fname);
   printf("Last name:   %s\n",empptr->lname);
   printf("Title:       %s\n",empptr->title);
   printf("Employee id: %d\n",empptr->emp_id);
}

