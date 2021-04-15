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
TEXT_COLOR = "Orange"
TEXT_LEFT = 10
TEXT_HEIGHT = 16

MESSAGES = (
        "F - fast animation",
        "R - reset animation",
        "",
        "W - walk around screen",
        "Esc - exit"
        )

sprite = Actor("sprite1.png")
BORDER = sprite.width/2 - 5
sprite.pos = (BORDER, HEIGHT/2)


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()

    y = 10
    for message in MESSAGES:
        screen.draw.text(message, (TEXT_LEFT, y), color=TEXT_COLOR)
        y += TEXT_HEIGHT


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
    if key == keys.R:
        sprite.x = BORDER
        sprite.y = HEIGHT/2
    if key == keys.F:
        animate(sprite, x=WIDTH-BORDER)
    if key == keys.W:
        animate(sprite, x=BORDER, y=BORDER, on_finished=a1)


def a1():
    animate(sprite, x=WIDTH-BORDER, on_finished=a2)


def a2():
    animate(sprite, y=HEIGHT-BORDER, on_finished=a3)


def a3():
    animate(sprite, x=BORDER, on_finished=a4)


def a4():
    animate(sprite, y=BORDER)
