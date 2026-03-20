#!/usr/bin/env python
# encoding=utf-8

"""Body Mass Index calculator."""

import sys


def compute_bmi(mass, height):
    """Vlastní výpočet BMI za základě hmotnosti a výšky."""
    height = height / 100.0
    bmi = mass / (height * height)
    return bmi


print("Mass (kg): ")
mass = int(input())

# kontrola na špatný vstup
if mass < 0:
    print("Invalid input")
    sys.exit(1)

print("Height (cm): ")
height = int(input())

# kontrola na špatný vstup
if height < 0:
    print("Invalid input")
    sys.exit(1)

# výpočet výsledku a výpis na obrazovku
print("BMI = ", compute_bmi(mass, height))
