#include <stdio.h>
#include <stdlib.h>

struct emp {
  int x;
  struct emp *next;
//struct emp *prev;
};

int main()
{
    int empIdValues[] = {2000, 1000, 5000, 8000, 7500}; 
    int count = sizeof(empIdValues)/sizeof(empIdValues[0]);

    // the root emp is the first emp 
    struct emp *root;       

    // current emp and a new emp 
    struct emp *currNode, *aNode;  

    root = malloc( sizeof(struct emp) );  
    root->x = empIdValues[0];
    root->next = NULL;
    currNode = root;

    for(int i=1; i<count; i++) 
    { 
       aNode = malloc( sizeof(struct emp) );  
       aNode->x = empIdValues[i];
       aNode->next = NULL;
       currNode->next = aNode;
       currNode = aNode;
    }

    currNode = root; 
    if(currNode != 0) 
    {
        int idx = 1;
        while(currNode)
        {
            printf("Employee %d has id: %d\n", idx, currNode->x); 
            currNode = currNode->next;
            ++idx;
        }
    }

    return 0;
}
