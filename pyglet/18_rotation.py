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
from pyglet.window import key
from pyglet.gl import glClear, glLoadIdentity, glColor3f, glVertex3f, glBegin, glEnd
from pyglet.gl import glClearColor, glPolygonMode, glDisable, glRotatef
from pyglet.gl import glViewport, glMatrixMode, glOrtho, gluLookAt
from pyglet.gl import GL_LINE, GL_COLOR_BUFFER_BIT, GL_MODELVIEW
from pyglet.gl import GL_FRONT, GL_BACK, GL_CULL_FACE, GL_PROJECTION, GL_QUADS, GL_TRIANGLES

r1 = 0.0
r2 = 0.0

window = pyglet.window.Window(width=500, height=500, caption="Pyglet+OpenGL")


keys = key.KeyStateHandler()
window.push_handlers(keys)


def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)  # barva pozadi obrazku
    glPolygonMode(GL_FRONT, GL_LINE)  # nastaveni rezimu vykresleni dratoveho modelu
    glPolygonMode(GL_BACK, GL_LINE)  # jak pro predni tak pro zadni steny
    glDisable(GL_CULL_FACE)  # zadne hrany ani steny se nebudou odstranovat


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)  # viditelna oblast pres cele okno


@window.event
def on_draw():
    global r1, r2

    if keys[key.LEFT]:
        r2 = r2 - 1
    if keys[key.RIGHT]:
        r2 = r2 + 1
    if keys[key.UP]:
        r1 = r1 - 1
    if keys[key.DOWN]:
        r1 = r1 + 1

    glClear(GL_COLOR_BUFFER_BIT)  # vymazani vsech bitovych rovin barvoveho bufferu

    glMatrixMode(GL_PROJECTION)  # zacatek modifikace projekcni matice
    glLoadIdentity()  # vymazani projekcni matice (=identita)
    glOrtho(-10, 10, -10, 10, -30, 30)  # nastaveni ortogonalni projekce
    glMatrixMode(GL_MODELVIEW)  # bude se menit modelova matice
    glLoadIdentity()  # nahrat jednotkovou matici

    gluLookAt(
        4.0,
        6.0,
        18.0,  # bod, odkud se kamera diva
        0.0,
        2.0,
        0.0,  # bod, kam se kamera diva
        0.0,
        1.0,
        0.0,
    )  # poloha "stropu" ve scene

    glRotatef(r1, 1.0, 0.0, 0.0)  # rotace objektu
    glRotatef(r2, 0.0, 1.0, 0.0)

    glBegin(GL_QUADS)  # vykresleni otevrene krychle - sten domecku
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-5.0, -5.0, -5.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(5.0, -5.0, 5.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(5.0, -5.0, -5.0)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(5.0, 5.0, 5.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(5.0, 5.0, -5.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-5.0, -5.0, -5.0)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-5.0, 5.0, -5.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(5.0, -5.0, -5.0)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(5.0, -5.0, 5.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(5.0, 5.0, 5.0)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(5.0, 5.0, -5.0)
    glEnd()

    glBegin(GL_TRIANGLES)  # vykresleni strechy domecku z trojuhelniku
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(5.0, 5.0, -5.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(5.0, 5.0, -5.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(5.0, 5.0, 5.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(5.0, 5.0, 5.0)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0, 11.0, 0.0)
    glEnd()


pyglet.app.run()
