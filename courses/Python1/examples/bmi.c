#include <stdio.h>

int main(void)
{
    float mass, height;
    float bmi;

    printf("Mass (kg): ");
    scanf("%f", &mass);

    printf("Height (cm): ");
    scanf("%f", &height);

    height = height / 100;

    bmi = mass / (height * height);
    printf("BMI = %10.2f\n", bmi);

    return 0;
}

