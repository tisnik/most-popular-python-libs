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

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Pyglet
#
# Příklad číslo 7: ukázka použití základních funkcí OpenGL
#                  další možnosti použití textového návěští
#
# ---------------------------------------------------------------------


# všechny třídy a funkce jsou obsaženy v jediném modulu nazvaném pyglet
import pyglet

# druhý import s funkcemi převzatými z OpenGL
from pyglet.gl import (
    GL_COLOR_BUFFER_BIT,
    GL_TRIANGLES,
    glBegin,
    glClear,
    glEnd,
    glLoadIdentity,
    glVertex2f,
)

# vytvoření okna
window = pyglet.window.Window(width=640, height=480, caption="Pyglet+OpenGL")


@window.event
def on_draw():
    """Obsluha události - překreslení obsahu okna."""
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
