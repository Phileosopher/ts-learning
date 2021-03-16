#define _POSIX_C_SOURCE 200809L 
#define __STDC_WANT_LIB_EXT1__ 1 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//------------------------------------------------------------------
// As with all bounds-checked functions, strncpy_s is only guaranteed 
// to be available if __STDC_LIB_EXT1__ is defined by the implementation 
// and if the user defines __STDC_WANT_LIB_EXT1__ to the integer constant 
// 1 before including string.h.
// gcc -D_POSIX_C_SOURCE=200809L CopyFunction2.c -o CopyFunction2 
//------------------------------------------------------------------

int main()
{
   char *src = "This is one line of text";
   char *dest;
   int len;
   len = strlen(src);

   dest = (char *)malloc(sizeof(src));

   // fill up 'dest'
 //strncpy_s(dest, len, src, len);
   strncpy(dest, src, len);

   // not required because 'strncpy' adds a null terminator:
 //dest[len-1] = '\0';

   printf("len:  %d\n", len);
   printf("src:  %s\n", src);
   printf("dest: %s\n", dest);
}

