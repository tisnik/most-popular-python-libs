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


import pygame

TITLE = "Raster image"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256


def _initialize_ui(title, width, height):
    """Initialize Pygame display, drawing surface, and clocks."""
    pygame.display.set_caption(title)
    display = pygame.display.set_mode([width, height])
    display.fill((0, 0, 0))
    clock = pygame.time.Clock()
    return (display, clock)


def _render_test_rgb_image(image, green):
    width, height = image.get_size()
    for y in range(height):
        for x in range(width):
            color = (x << 16) + (green << 8) + y
            image.set_at((x, y), color)


def _main():
    display, clock = _initialize_ui(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
    image1 = pygame.Surface([IMAGE_WIDTH, IMAGE_HEIGHT])
    image2 = pygame.Surface([IMAGE_WIDTH, IMAGE_HEIGHT])

    _render_test_rgb_image(image1, 0)
    _render_test_rgb_image(image2, 255)


if __name__ == "__main__":
    _main()


# finito
