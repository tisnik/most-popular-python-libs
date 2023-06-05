#include <stdio.h>

#include "array_printer.h"

extern void print_array(float array[], int items)
{
    int i;
    for (i=0; i<items; i++) {
        printf("array item %d = %f\n", i, array[i]);
    }
}
