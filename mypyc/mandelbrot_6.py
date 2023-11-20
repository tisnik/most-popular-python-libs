import palette_mandmap
from sys import argv

from typing import Tuple


def calc_mandelbrot(width: int, height: int, maxiter: int, palette: Tuple[Tuple[int, int, int], ...]) -> None:
    print("P3")
    print("{w} {h}".format(w=width, h=height))
    print("255")

    cy = -1.5
    for y in range(0, height):
        cx = -2.0
        for x in range(0, width):
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

            r = palette[i % 256][0]
            g = palette[i % 256][1]
            b = palette[i % 256][2]
            print("{r} {g} {b}".format(r=r, g=g, b=b))
            cx += 3.0/width
        cy += 3.0/height


if len(argv) < 4:
    width = 512
    height = 512
    maxiter = 255
else:
    width = int(argv[1])
    height = int(argv[2])
    maxiter = int(argv[3])
calc_mandelbrot(width, height, maxiter, palette_mandmap.palette)
