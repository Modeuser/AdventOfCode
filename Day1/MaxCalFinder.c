#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE * fPointer;
    fPointer = fopen("CalLog.txt", "r");
    int newlineCounter = 0;
    char currentValue[150];
    
    while(!feof(fPointer)){
        fgets(currentValue, 150, fPointer);
        puts(currentValue);
        //"puts" current works by displaying the correct numbers
    }

    printf("%d", newlineCounter);

    fclose(fPointer);

    return 0;

}