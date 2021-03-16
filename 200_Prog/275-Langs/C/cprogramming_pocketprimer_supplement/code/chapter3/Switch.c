#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    // seed the random number generator:
    srand(time(NULL));

    int rnd = rand() % 6 + 1;

    switch(rnd)
    {
        case 1:   printf("ONE\n");
                  break;
        case 2:   printf("TWO\n");
                  break;
        case 3:   printf("THREE\n");
                  break;
        case 4:   printf("FOUR\n");
                  break;
        case 5:   printf("FIVE\n");
                  break;
        case 6:   printf("SIX\n");
                  break;
        default:  printf("Other value\n");
    }

    return 0;
}

