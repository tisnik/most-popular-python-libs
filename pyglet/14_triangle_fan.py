#!/usr/bin/env python
# vim: set fileencoding=utf-8

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

# Demonstrační příklady využívající knihovnu Pyglet

import pyglet
from pyglet.gl import glClear, glLoadIdentity, glColor3f, glVertex2i, glBegin, glEnd
from pyglet.gl import glClearColor, glPolygonMode
from pyglet.gl import GL_LINE, GL_TRIANGLE_FAN, GL_FILL, GL_COLOR_BUFFER_BIT, GL_FRONT_AND_BACK

# vytvoření okna
window = pyglet.window.Window(width=450, height=350, caption="Pyglet+OpenGL")


def draw_triangle_fan(x, y):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0)  # kazdy vertex bude vykresleny jinou barvou
    glVertex2i(x + 175, y)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(x + 50, y + 80)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(x + 100, y + 80)
    glColor3f(1.0, 1.0, 0.0)  # kazdy vertex bude vykresleny jinou barvou
    glVertex2i(x + 150, y + 80)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2i(x + 200, y + 80)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2i(x + 250, y + 80)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(x + 300, y + 80)
    glEnd()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glClearColor(0.0, 0.0, 0.0, 0.0)  # nastaveni mazaci barvy na cernou
    glClear(GL_COLOR_BUFFER_BIT)  # vymazani bitovych rovin barvoveho bufferu

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    draw_triangle_fan(50, 50)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    draw_triangle_fan(50, 200)


pyglet.app.run()
