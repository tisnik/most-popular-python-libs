"""Fresnel fractal generator."""

from turtle import *
from math import *


home()
hideturtle()
tracer(100, 0)

x = 0.0
y = 0.0
f = 0.0

while f < 5000:
    f += 0.2
    x += cos(f * f)
    y += sin(f * f)
    goto(2 * x, 2 * y)
    dot(1)

exitonclick()
