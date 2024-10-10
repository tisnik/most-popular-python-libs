"""Fresnel fractal generator."""

#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from math import *
from turtle import *

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
