#include <stdio.h>

typedef struct {
    unsigned int a;
    unsigned int b;
    unsigned int c;
} my_struct;

void test_pass_by_value(my_struct s) {
    printf("a=%u\nb=%u\nc=%u\n", s.a, s.b, s.c);
}

void test_pass_by_reference(my_struct *s) {
    printf("a=%u\nb=%u\nc=%u\n", s->a, s->b, s->c);
}
