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
RED = (255, 128, 128, 255)


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def make_sprite(filename, window):
    image_stream = open("gnome-globe.png", "rb")
    image = pyglet.image.load("gnome-globe.png", file=image_stream)

    # stred spritu bude odpovidat stredu obrazku - sprite se nam bude
    # mnohem lepe pozicovat
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

    sprite = pyglet.sprite.Sprite(image)
    # vycentrovani spritu
    sprite.x = window.width / 2 - image.width / 2
    sprite.y = window.height / 2 - image.height / 2
    sprite.step = 5
    return sprite


window = create_window(640, 480)
sprite = make_sprite("gnome-globe.png", window)


@window.event
def on_draw():
    window.clear()
    sprite.draw()


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & pyglet.window.mouse.LEFT:
        sprite.x = x
        sprite.y = y


pyglet.app.run()
