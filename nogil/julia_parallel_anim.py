#!/usr/bin/env python

"""Renderer of the classic Julia fractal."""

import math
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from time import perf_counter

from PIL import Image

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


def julia(cx, cy, zx, zy, maxiter):
    c = complex(cx, cy)
    z = complex(zx, zy)
    for i in range(0, maxiter):
        if abs(z) > 2:
            return i
        z = z * z + c
    return 0


def recalc_fractal(filename, palette, xmin, ymin, xmax, ymax, cx, cy, maxiter=1000):
    """Recalculate the whole fractal and render the set into given image."""
    t1 = perf_counter()
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))

    width, height = image.size
    stepx = (xmax - xmin) / width
    stepy = (ymax - ymin) / height

    y1 = ymin
    for y in range(0, height):
        x1 = xmin
        for x in range(0, width):
            i = julia(cx, cy, x1, y1, maxiter)
            i = 3 * i % 256
            color = (palette[i][0], palette[i][1], palette[i][2])
            image.putpixel((x, y), color)
            x1 += stepx
        y1 += stepy

    image.save(filename)
    t2 = perf_counter()
    # print("Done", filename, t2-t1)


def main(threads):
    import palette_mandmap

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            cx = 1.0 * math.cos(rad)
            cy = 1.0 * math.sin(rad)
            filename = f"anim_{angle:03d}.png"
            # print(filename)

            executor.submit(recalc_fractal, filename, palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, cx, cy, 1000)


if __name__ == "__main__":
    threads = 8
    if len(sys.argv) > 1:
        threads = int(sys.argv[1])

    t1 = perf_counter()
    main(threads)
    t2 = perf_counter()
    print(f"Threads: {threads}   Rendering time: {t2-t1} seconds")
