#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Employee
{
   char  fname [50];
   char  lname [50];
   char  title [100];
   int   emp_id;
} emp;

int main(int argc, char **argv)
{
   int empCount = 5;
   struct Employee emps[empCount];
   struct Employee *empPtr;

   char *fnames[3] = {"John", "Jane", "Steve"};
   char *lnames[4] = {"Smith", "Jones", 
                    "Edwards", "Anderson"};
   char *titles[4] = {"Sales", "Marketing", 
                    "Development", "Support"};

   // initialize array of Employees
   for(int i=0; i<empCount; i++)
   {
      strcpy(emps[i].fname, fnames[i%3]);
      strcpy(emps[i].lname, lnames[i%4]);
      strcpy(emps[i].title, titles[i%4]);
      emps[i].emp_id = 1000*(i+1);
   }

   // print contents of all Employees
   for(int i=0; i<empCount; i++)
   {
      printf("First name:  %s\n",emps[i].fname);
      printf("Last name:   %s\n",emps[i].lname);
      printf("Title:       %s\n",emps[i].title);   
      printf("Employee id: %d\n",emps[i].emp_id);
      printf("\n");
   }

   // print contents of all Employees
   for(int i=0; i<empCount; i++)
   {
      empPtr = &emps[i];

      printf("First name:  %s\n",empPtr->fname);
      printf("Last name:   %s\n",empPtr->lname);
      printf("Title:       %s\n",empPtr->title);   
      printf("Employee id: %d\n",empPtr->emp_id);
      printf("\n");
   }
}

