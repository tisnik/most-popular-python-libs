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

# taken from Fractint
palette = (
        (255, 255, 255), (224, 224, 224), (216, 216, 216), (208, 208, 208),
        (200, 200, 200), (192, 192, 192), (184, 184, 184), (176, 176, 176),
        (168, 168, 168), (160, 160, 160), (152, 152, 152), (144, 144, 144),
        (136, 136, 136), (128, 128, 128), (120, 120, 120), (112, 112, 112),
        (104, 104, 104),  (96,  96,  96),  (88,  88,  88),  (80,  80,  80),
        (72,   72,  72),  (64,  64,  64),  (56,  56,  56),  (48,  48,  56),
        (40,   40,  56),  (32,  32,  56),  (24,  24,  56),  (16,  16,  56),
        (8,     8,  56), (000, 000,  60), (000, 000,  64), (000, 000,  72),
        (000, 000,  80), (000, 000,  88), (000, 000,  96), (000, 000, 104),
        (000, 000, 108), (000, 000, 116), (000, 000, 124), (000, 000, 132),
        (000, 000, 140), (000, 000, 148), (000, 000, 156), (000, 000, 160),
        (000, 000, 168), (000, 000, 176), (000, 000, 184), (000, 000, 192),
        (000, 000, 200), (000, 000, 204), (000, 000, 212), (000, 000, 220),
        (000, 000, 228), (000, 000, 236), (000, 000, 244), (000, 000, 252),
        (000,   4, 252),   (4,  12, 252),   (8,  20, 252),  (12,  28, 252),
        (16,   36, 252),  (20,  44, 252),  (20,  52, 252),  (24,  60, 252),
        (28,   68, 252),  (32,  76, 252),  (36,  84, 252),  (40,  92, 252),
        (40,  100, 252),  (44, 108, 252),  (48, 116, 252),  (52, 120, 252),
        (56,  128, 252),  (60, 136, 252),  (60, 144, 252),  (64, 152, 252),
        (68,  160, 252),  (72, 168, 252),  (76, 176, 252),  (80, 184, 252),
        (80,  192, 252),  (84, 200, 252),  (88, 208, 252),  (92, 216, 252),
        (96,  224, 252), (100, 232, 252), (100, 228, 248),  (96, 224, 244),
        (92,  216, 240),  (88, 212, 236),  (88, 204, 232),  (84, 200, 228),
        (80,  192, 220),  (76, 188, 216),  (76, 180, 212),  (72, 176, 208),
        (68,  168, 204),  (64, 164, 200),  (64, 156, 196),  (60, 152, 188),
        (56,  144, 184),  (52, 140, 180),  (52, 132, 176),  (48, 128, 172),
        (44,  120, 168),  (40, 116, 160),  (40, 108, 156),  (36, 104, 152),
        (32,   96, 148),  (28,  92, 144),  (28,  84, 140),  (24,  80, 136),
        (20,   72, 128),  (16,  68, 124),  (16,  60, 120),  (12,  56, 116),
        (8,    48, 112),   (4,  44, 108), (000,  36, 100),   (4,  36, 104),
        (12,   40, 108),  (16,  44, 116),  (24,  48, 120),  (28,  52, 128),
        (36,   56, 132),  (40,  60, 140),  (48,  64, 144),  (52,  64, 148),
        (60,   68, 156),  (64,  72, 160),  (72,  76, 168),  (76,  80, 172),
        (84,   84, 180),  (88,  88, 184),  (96,  92, 192), (104, 100, 192),
        (112, 112, 196), (124, 120, 200), (132, 132, 204), (144, 140, 208),
        (152, 152, 212), (164, 160, 216), (172, 172, 220), (180, 180, 224),
        (192, 192, 228), (200, 200, 232), (212, 212, 236), (220, 220, 240),
        (232, 232, 244), (240, 240, 248), (252, 252, 252), (252, 240, 244),
        (252, 224, 232), (252, 208, 224), (252, 192, 212), (252, 176, 204),
        (252, 160, 192), (252, 144, 184), (252, 128, 172), (252, 112, 164),
        (252,  96, 152), (252,  80, 144), (252,  64, 132), (252,  48, 124),
        (252,  32, 112), (252,  16, 104), (252, 000,  92), (236, 000,  88),
        (228, 000,  88), (216,   4,  84), (204,   4,  80), (192,   8,  76),
        (180,   8,  76), (168,  12,  72), (156,  16,  68), (144,  16,  64),
        (132,  20,  60), (124,  20,  60), (112,  24,  56), (100,  24,  52),
        (88,   28,  48),  (76,  32,  44),  (64,  32,  44),  (52,  36,  40),
        (40,   36,  36),  (28,  40,  32),  (16,  44,  28),  (20,  52,  32),
        (24,   60,  36),  (28,  68,  44),  (32,  76,  48),  (36,  88,  56),
        (40,   96,  60),  (44, 104,  64),  (48, 112,  72),  (52, 120,  76),
        (56,  132,  84),  (48, 136,  84),  (40, 144,  80),  (52, 148,  88),
        (68,  156, 100),  (80, 164, 112),  (96, 168, 124), (108, 176, 136),
        (124, 184, 144), (136, 192, 156), (152, 196, 168), (164, 204, 180),
        (180, 212, 192), (192, 220, 200), (208, 224, 212), (220, 232, 224),
        (236, 240, 236), (252, 248, 248), (252, 252, 252), (252, 252, 240),
        (252, 252, 228), (252, 252, 216), (248, 248, 204), (248, 248, 192),
        (248, 248, 180), (248, 248, 164), (244, 244, 152), (244, 244, 140),
        (244, 244, 128), (244, 244, 116), (240, 240, 104), (240, 240,  92),
        (240, 240,  76), (240, 240,  64), (236, 236,  52), (236, 236,  40),
        (236, 236,  28), (236, 236,  16), (232, 232,   0), (232, 232,  12),
        (232, 232,  28), (232, 232,  40), (236, 236,  56), (236, 236,  68),
        (236, 236,  84), (236, 236,  96), (240, 240, 112), (240, 240, 124),
        (240, 240, 140), (244, 244, 152), (244, 244, 168), (244, 244, 180),
        (244, 244, 196), (248, 248, 208), (248, 248, 224), (248, 248, 236),
        (252, 252, 252), (248, 248, 248), (240, 240, 240), (232, 232, 232))
from sys import argv


def calc_mandelbrot(width, height, maxiter, palette):
    print("P3")
    print("{w} {h}".format(w=width, h=height))
    print("255")

    cy = -1.5
    for y in range(height):
        cx = -2.0
        for x in range(width):
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

            r = palette[i][0]
            g = palette[i][1]
            b = palette[i][2]
            print("{r} {g} {b}".format(r=r, g=g, b=b))
            cx += 3.0/width
        cy += 3.0/height


if __name__ == "__main__":
    if len(argv) < 4:
        width = 512
        height = 512
        maxiter = 255
    else:
        width = int(argv[1])
        height = int(argv[2])
        maxiter = int(argv[3])
    calc_mandelbrot(width, height, maxiter, palette)
