import palette_mandmap
from sys import argv, exit
import cython
from cpython cimport array
from libc.stdio cimport printf


@cython.cdivision(True)
cdef void calc_mandelbrot(int width, int height, int maxiter, unsigned char *palette) nogil:
    cdef double zx
    cdef double zy
    cdef double zx2
    cdef double zy2
    cdef double cx
    cdef double cy
    cdef unsigned char r
    cdef unsigned char g
    cdef unsigned char b
    cdef int i
    cdef int index

    printf("P3\n%d %d\n255\n", width, height)
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

            index = i * 3
            r = palette[index]
            g = palette[index+1]
            b = palette[index+2]
            printf("%d %d %d\n", r, g, b)
            cx += 3.0/width
        cy += 3.0/height


cdef array.array palette = array.array('B')

if __name__ == "__main__":

    if len(argv) < 4:
        print("usage: python mandelbrot width height maxiter")
        exit(1)

    for color in palette_mandmap.palette:
        for component in color:
            palette.append(component)

    width = int(argv[1])
    height = int(argv[2])
    maxiter = int(argv[3])
    calc_mandelbrot(width, height, maxiter, palette.data.as_uchars)
