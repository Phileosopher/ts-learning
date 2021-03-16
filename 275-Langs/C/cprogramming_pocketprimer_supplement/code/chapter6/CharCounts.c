#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main()
{
   char ch, str1[] = "This is a string with some short words that wraps around and let's see how well the code in this code sample actually works!";

   int len1 = strlen(str1);

   // incorrect:
   // int *chars = malloc (sizeof (char) * len1); 
   // correct:
   char *chars = malloc (sizeof (char) * len1); 
   int *counts = malloc (sizeof (int) * len1); 
   int i;

   for (i=0; i<len1; i++)
   {
     counts[i] = 0;
     chars[i]  = ' ';
   }

   int pos=0, foundchar=0;
   counts[pos] = 1;
   chars[pos]  = str1[0];
   pos = 1;

   for(int i=1; i<len1; i++)
   {
      ch = str1[i];
    //printf("checking char %c at pos: %d\n",ch, i);

      foundchar = 0;
      for(int k=0; k<pos; k++)
      {
         if(ch == chars[k])
         { 
            ++counts[k];
 //printf("count for %c at pos %d : %d\n",ch, k, counts[k]);
            foundchar = 1;
            break;
         } 
      }
   
      if(foundchar == 0)
      { 
 //printf("inserting char %c at pos: %d\n",ch, pos);
         counts[pos] = 1;
         chars[pos]  = ch;
         ++pos;
      } 
   }

   printf("Full string: %s\n",str1);

   char ch2;
   int count;
   for(int k=0; k<pos; k++)
   {
      printf("char %c count %d at array position: %d\n",chars[k], counts[k], k);
   }

   return 0;
}
