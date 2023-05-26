#include <stdio.h>

#include "greeter.h"

extern void greet(char *x) {
    printf("Hello %s!\n", x);
}
