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

import sys
from ctypes import CDLL, c_double, c_int, create_string_buffer

from palette_mandmap import palette

import pygame
import pygame.locals

TITLE = "Renderer"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


def initialize_ui(title, width, height):
    """Initialize Pygame display, drawing surface, and clocks."""
    # set window title
    pygame.display.set_caption(title)

    # initialize window
    display = pygame.display.set_mode([width, height])
    display.fill((0, 0, 0))

    clock = pygame.time.Clock()

    return display, clock


def event_loop(display, image1, image2, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # all events has been processed - update scene and redraw the screen
        display.blit(image1, (30, 20))
        display.blit(image2, (60 + image1.get_width(), 20))

        # and update the whole display
        pygame.display.update()
        clock.tick(25)


def palette_to_buffer(p):
    s = create_string_buffer(len(p) * 3)
    i = 0
    for color in p:
        s[i] = color[0]
        s[i + 1] = color[1]
        s[i + 2] = color[2]
        i += 3
    return s


def image_from_buffer(buffer, width, height, fmt):
    return pygame.image.frombytes(bytes(buffer), (width, height), fmt)


def main():
    pal = palette_to_buffer(palette)

    display, clock = initialize_ui(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)

    # try to load dynamically linked library
    renderer = CDLL("./renderer.so")

    # create buffer for raster image
    buffer = create_string_buffer(4 * IMAGE_WIDTH * IMAGE_HEIGHT)

    renderer.render_mandelbrot(c_int(IMAGE_WIDTH), c_int(IMAGE_HEIGHT), pal, buffer)
    image1 = image_from_buffer(buffer, IMAGE_WIDTH, IMAGE_HEIGHT, "RGBX")

    renderer.render_julia(
        c_int(IMAGE_WIDTH),
        c_int(IMAGE_HEIGHT),
        pal,
        buffer,
        c_double(0.285),
        c_double(0.01),
    )
    image2 = image_from_buffer(buffer, IMAGE_WIDTH, IMAGE_HEIGHT, "RGBX")

    event_loop(display, image1, image2, clock)


if __name__ == "__main__":
    main()


# finito
