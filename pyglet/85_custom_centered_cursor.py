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


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def load_cursor(filename):
    image = pyglet.image.load(filename)
    return pyglet.window.ImageMouseCursor(image, image.width / 2, image.height / 2)


window = create_window(640, 480)
cursor = load_cursor("gnome-globe.png")
window.set_mouse_cursor(cursor)


@window.event
def on_draw():
    window.clear()


pyglet.app.run()
