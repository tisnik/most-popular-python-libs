#!/usr/bin/env python

"""Renderer of the classic Julia fractal."""

from concurrent.futures.thread import ThreadPoolExecutor
from PIL import Image
from time import perf_counter

IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 1024


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
    print("Done", filename, t2-t1)


def main():
    import palette_mandmap

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(recalc_fractal, "spiral_1.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, -0.769824999999999998320, -0.109270000000000000000, 1000)
        executor.submit(recalc_fractal, "spiral_2.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, -0.171119200000000013445, 0.657309400000000000000, 1000)
        executor.submit(recalc_fractal, "spiral_3.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, -0.207190825000000012496, 0.676656624999999999983, 1000)
        executor.submit(recalc_fractal, "spiral_4.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, -0.540623850000000003876, 0.523798050000000000019, 1000)
        executor.submit(recalc_fractal, "julia1.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, 0.0, 1.0, 1000)
        executor.submit(recalc_fractal, "julia2.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, -1.0, 0.0, 500)
        executor.submit(recalc_fractal, "julia3.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, 0.285, 0.01, 1000)
        executor.submit(recalc_fractal, "julia4.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, -0.4, 0.6, 1000)
        executor.submit(recalc_fractal, "julia5.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, -0.835, -0.2321, 1000)
        executor.submit(recalc_fractal, "julia6.png", palette_mandmap.palette, -1.5, -1.5, 1.5, 1.5, 0.4, 0.4, 1000)


if __name__ == "__main__":
    t1 = perf_counter()
    main()
    t2 = perf_counter()
    print(f"Rendering time: {t2-t1} seconds")
