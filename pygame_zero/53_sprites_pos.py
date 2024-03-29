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

BACKGROUND_COLOR = (0, 0x40, 0x40)

red_sprite = Actor("red.gif")
red_sprite.pos = (120, 240)

blue_sprite = Actor("blue.gif")
blue_sprite.pos = (240, 240)

yellow_sprite = Actor("yellow.gif")
yellow_sprite.pos = (360, 240)


def draw_sprite_pos(which, sprite, pos_x, pos_y, color):
    screen.draw.text(which + ":", (pos_x, pos_y), color=color)
    screen.draw.text(str(int(sprite.x)), (pos_x + 70, pos_y), color=color)
    screen.draw.text(str(int(sprite.y)), (pos_x + 110, pos_y), color=color)


def draw():
    screen.fill(BACKGROUND_COLOR)
    red_sprite.draw()
    blue_sprite.draw()
    yellow_sprite.draw()

    draw_sprite_pos("Red", red_sprite, 10, 10, "#db0000")
    draw_sprite_pos("Blue", blue_sprite, 10, 30, "#00a2db")
    draw_sprite_pos("Yellow", yellow_sprite, 10, 50, "#dbc500")
