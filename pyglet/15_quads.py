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
from pyglet.gl import glClear, glLoadIdentity, glColor3f, glVertex2i, glBegin, glEnd
from pyglet.gl import glClearColor, glPolygonMode, glEnable, glDisable
from pyglet.gl import glPointSize, glLineWidth, glPolygonStipple, GLubyte
from pyglet.gl import GL_POINT, GL_LINE, GL_QUADS, GL_FILL, GL_COLOR_BUFFER_BIT
from pyglet.gl import GL_FRONT_AND_BACK, GL_POINT_SMOOTH, GL_LINE_SMOOTH, GL_POLYGON_STIPPLE

window = pyglet.window.Window(width=450, height=350, caption="Pyglet+OpenGL")


def draw_quad(x, y):
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # kazdy vertex bude vykresleny jinou barvou
    glVertex2i(x, y)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(x + 100, y)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(x + 100, y + 100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(x, y + 100)
    glEnd()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    pattern1 = [  # prvni vyplnovy vzorek
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x03,
        0x80,
        0x01,
        0xC0,
        0x06,
        0xC0,
        0x03,
        0x60,
        0x04,
        0x60,
        0x06,
        0x20,
        0x04,
        0x30,
        0x0C,
        0x20,
        0x04,
        0x18,
        0x18,
        0x20,
        0x04,
        0x0C,
        0x30,
        0x20,
        0x04,
        0x06,
        0x60,
        0x20,
        0x44,
        0x03,
        0xC0,
        0x22,
        0x44,
        0x01,
        0x80,
        0x22,
        0x44,
        0x01,
        0x80,
        0x22,
        0x44,
        0x01,
        0x80,
        0x22,
        0x44,
        0x01,
        0x80,
        0x22,
        0x44,
        0x01,
        0x80,
        0x22,
        0x44,
        0x01,
        0x80,
        0x22,
        0x66,
        0x01,
        0x80,
        0x66,
        0x33,
        0x01,
        0x80,
        0xCC,
        0x19,
        0x81,
        0x81,
        0x98,
        0x0C,
        0xC1,
        0x83,
        0x30,
        0x07,
        0xE1,
        0x87,
        0xE0,
        0x03,
        0x3F,
        0xFC,
        0xC0,
        0x03,
        0x31,
        0x8C,
        0xC0,
        0x03,
        0x33,
        0xCC,
        0xC0,
        0x06,
        0x64,
        0x26,
        0x60,
        0x0C,
        0xCC,
        0x33,
        0x30,
        0x18,
        0xCC,
        0x33,
        0x18,
        0x10,
        0xC4,
        0x23,
        0x08,
        0x10,
        0x63,
        0xC6,
        0x08,
        0x10,
        0x30,
        0x0C,
        0x08,
        0x10,
        0x18,
        0x18,
        0x08,
        0x10,
        0x00,
        0x00,
        0x08,
    ]

    pattern1_gl = (GLubyte * len(pattern1))(*pattern1)

    pattern2 = [  # druhy vyplnovy vzorek
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
        0x55,
        0x55,
        0x55,
        0x55,
        0xAA,
        0xAA,
        0xAA,
        0xAA,
    ]

    pattern2_gl = (GLubyte * len(pattern2))(*pattern2)

    glClearColor(0.0, 0.0, 0.0, 0.0)  # nastaveni mazaci barvy na cernou
    glClear(GL_COLOR_BUFFER_BIT)  # vymazani bitovych rovin barvoveho bufferu

    glPointSize(5.0)  # velikost bodu je rovna peti pixelum
    glLineWidth(2.0)  # tloustka usecek je rovna dvema pixelum
    glEnable(GL_POINT_SMOOTH)  # povoleni antialiasingu bodu
    glEnable(GL_LINE_SMOOTH)  # povoleni antialiasingu usecek
    glDisable(GL_POLYGON_STIPPLE)  # zakazat vzorek
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # vykreslovani vyplnenych ctyruhelniku
    draw_quad(50, 50)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  # vykreslovani pouze hran ctyruhelniku
    draw_quad(180, 50)
    glPolygonMode(
        GL_FRONT_AND_BACK, GL_POINT
    )  # vykreslovani pouze vrcholu ctyruhelniku
    draw_quad(310, 50)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # vykreslovani vyplnenych ctyruhelniku
    glEnable(GL_POLYGON_STIPPLE)  # povolit vzorek
    glPolygonStipple(pattern1_gl)  # zadat prvni vzorek
    draw_quad(110, 190)
    glPolygonStipple(pattern2_gl)  # zadat druhy vzorek
    draw_quad(240, 190)


pyglet.app.run()
