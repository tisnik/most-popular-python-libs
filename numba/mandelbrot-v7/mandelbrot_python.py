#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from sys import argv

import palette_mandmap

import numpy as np
from numba import jit, prange
from numba.types import UniTuple, int64


@jit(nopython=True)
def calc_pixel(maxiter, cx, cy):
    zx = 0.0
    zy = 0.0
    i = 0
    while i < maxiter:
        zx2 = zx * zx
        zy2 = zy * zy
        if zx2 + zy2 > 4.0:
            break
        zy = 2.0 * zx * zy + cy
        zx = zx2 - zy2 + cx
        i += 1
    return i


@jit((int64, int64, int64, UniTuple(UniTuple(int64, 3), 256)), nopython=True, parallel=True)
def calc_mandelbrot(width, height, maxiter, palette):
    iters = np.empty((height, width), dtype=np.uint8)

    # calc part
    for y in prange(0, height):
        cy = -1.5 + 3.0*y/height
        cx = -2.0
        for x in range(width):
            i = calc_pixel(maxiter, cx, cy)
            iters[y][x] = i

            cx += 3.0/width
        cy += 3.0/height

    # image export part
    print("P3")
    print(width)
    print(height)
    print("255")
    for y in range(height):
        for x in range(width):
            i = iters[y][x]
            r = palette[i % 256][0]
            g = palette[i % 256][1]
            b = palette[i % 256][2]
            print(r)
            print(g)
            print(b)


if __name__ == "__main__":
    if len(argv) < 4:
        width = 512
        height = 512
        maxiter = 255
    else:
        width = int(argv[1])
        height = int(argv[2])
        maxiter = int(argv[3])
    calc_mandelbrot(width, height, maxiter, palette_mandmap.palette)
    # calc_mandelbrot.parallel_diagnostics(level=4)
