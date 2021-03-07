#include <stdio.h>
#include <string.h>
 
struct Address
{
   char street[50];
   char city[50];
};
 
struct Employee
{
   int id;
   char name[20];
   char title[20];
   struct Address address;
} emp;
 
int main(int argc, char **argv)
{
   struct Employee emp = 
     {1000, "John Smith", "Developer", "123 Main Street", "Chicago"};

   printf("Emp Id: %d \n",   emp.id);
   printf("Name:   %s \n",   emp.name);
   printf("Title:  %s \n\n", emp.title);

   printf("Street: %s\n", emp.address.street);
   printf("City:   %s\n", emp.address.city);
   return 0;
}

