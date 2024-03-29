#!/usr/bin/env python

#
#  (C) Copyright 2017  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import pyglet

GRAY = (128, 128, 128, 255)


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def create_gray_label(text, x, y, anchor_x, anchor_y):
    return pyglet.text.Label(
        text, font_size=18, x=x, y=y, anchor_x=anchor_x, anchor_y=anchor_y, color=GRAY
    )


window = create_window(640, 480)
label = create_gray_label("Playing", 10, 10, "left", "bottom")


@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.options["audio"] = ("pulse", "openal", "silent")

source = pyglet.media.load("login.wav", streaming=False)

source.play()
pyglet.app.run()
