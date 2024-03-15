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

import pygame
import pygame.locals

TITLE = "Raster image"
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


def render_test_rgb_image(image, green):
    width, height = image.get_size()
    for y in range(height):
        for x in range(width):
            color = (x<<16) + (green<<8) + y
            image.set_at((x, y), color)


def main():
    display, clock = initialize_ui(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
    image1 = pygame.Surface([IMAGE_WIDTH, IMAGE_HEIGHT])
    image2 = pygame.Surface([IMAGE_WIDTH, IMAGE_HEIGHT])

    render_test_rgb_image(image1, 0)
    render_test_rgb_image(image2, 255)

    event_loop(display, image1, image2, clock)


if __name__ == "__main__":
    main()


# finito
