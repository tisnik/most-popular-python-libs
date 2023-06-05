#include <stdio.h>

#include "array_printer.h"

extern void print_array(vector_t array[], int items)
{
    int i;
    for (i=0; i<items; i++) {
        printf("array item %d = (%f, %f, %f)\n",
                i, array[i].x, array[i].y, array[i].z);
    }
}
