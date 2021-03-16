# do not change the order of the next two lines:
gcc -std=c11 -Wall                       -c FindChar2.c
gcc -std=c11 FindChar2.o FindMain2.c     -o FindMain2 
gcc -std=c11 Hello2.c                    -o Hello2
gcc -std=c11 HelloWorld.c                -o HelloWorld
gcc -std=c11 -Wall                       -c depend1.c
gcc -std=c11 -Wall                       -c depend2.c
gcc -std=c11 depend1.o depend2.o main1.c -o main1

echo ""
echo "Files containing strcpy:"
grep -l strcpy *.c

echo ""
echo "Files containing strncpy:"
grep -l strncpy *.c

