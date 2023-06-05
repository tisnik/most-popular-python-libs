#include <stdio.h>

#include "array_printer.h"

#define COLUMNS 3

extern void print_array(float array[][COLUMNS], int rows)
{
    int i, j;
    for (j=0; j<rows; j++) {
        float *row = array[j];
        for (i=0; i<COLUMNS; i++) {
            printf("%3.2f ", row[i]);
        }
        putchar('\n');
    }
}
