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

import math

import pyglet

window = pyglet.window.Window(width=640, height=480, caption="Pyglet library")

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load("gnome-globe.png", file=image_stream)

image.anchor_x = image.width / 2
image.anchor_y = image.height / 2

sprite = pyglet.sprite.Sprite(image)
sprite.x = window.width / 2
sprite.y = window.height / 2
sprite.t = 0


@window.event
def on_draw():
    window.clear()
    sprite.draw()


def update(dt):
    sprite.t += 1
    sprite.scale = 5.0 * math.sin(sprite.t / 10.0)


pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
