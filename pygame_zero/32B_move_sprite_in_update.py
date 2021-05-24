#
#  (C) Copyright 2020  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)

sprite = Actor("sprite1.png")
sprite.pos = (240, 240)
dx = 0
dy = 0


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()


def update():
    sprite.left += dx
    sprite.top += dy


directions = {
        keys.UP: (0, -1),
        keys.DOWN: (0, 1),
        keys.LEFT: (-1, 0),
        keys.RIGHT: (1, 0),
        }


def on_key_down(key, mod, unicode):
    global dx, dy
    if key == keys.ESCAPE:
        exit()
    if key in directions:
        dx, dy = directions[key]
