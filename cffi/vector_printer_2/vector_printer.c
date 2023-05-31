#include <stdio.h>

#include "vector_printer.h"

extern void print_vector(vector_t *v)
{
    printf("Vector (%.1f  %.1f  %.1f)\n", v->x, v->y, v->z);
}
