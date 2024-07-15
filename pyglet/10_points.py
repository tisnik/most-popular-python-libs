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
# Příklad číslo 10: ukázka použití základních funkcí OpenGL
#                   základní vlastnosti bodů (points)
#
# ---------------------------------------------------------------------

# všechny třídy a funkce jsou obsaženy v jediném modulu nazvaném pyglet
import pyglet

# druhý import s funkcemi převzatými z OpenGL
from pyglet.gl import GL_COLOR_BUFFER_BIT, GL_POINT_SMOOTH, GL_POINTS, glBegin, glClear, glColor3f, glDisable, glEnable, glEnd, glLoadIdentity, glPointSize, glVertex2f

# vytvoření okna
window = pyglet.window.Window(width=450, height=350, caption="Pyglet+OpenGL")


@window.event
def on_draw():
    """Obsluha události - překreslení obsahu okna."""
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glDisable(GL_POINT_SMOOTH)  # zakazani antialiasingu bodu
    glPointSize(1.0)  # velikost vykreslovanych bodu je jeden pixel
    glBegin(GL_POINTS)
    for i in xrange(0, 10):  # vykresleni prvni rady bodu ruzne barvy
        step = i / 10.0
        glColor3f(
            step, 0.5, 1.0 - step
        )  # zmena barvy uvnitr prikazovych "zavorek" glBegin()/glEnd()
        glVertex2f(50.0 + 300.0 * step, 50.0)
    glEnd()

    glDisable(GL_POINT_SMOOTH)  # zakazani antialiasingu bodu
    for i in range(10):  # vykresleni druhe rady bodu ruzne velikosti a barvy
        step = i / 10.0
        glColor3f(
            step, 0.5, 1.0 - step
        )  # zmena barvy vne prikazovych "zavorek" glBegin()/glEnd()
        glPointSize(step * 20.0 + 1.0)  # zmena velikosti vykreslovanych bodu
        glBegin(GL_POINTS)
        glVertex2f(50.0 + 300.0 * step, 100.0)
        glEnd()

    glEnable(GL_POINT_SMOOTH)  # povoleni antialiasingu bodu
    for i in range(10):  # vykresleni treti rady bodu ruzne velikosti a barvy
        step = i / 10.0
        glColor3f(
            step, 0.5, 1.0 - step
        )  # zmena barvy vne prikazovych "zavorek" glBegin()/glEnd()
        glPointSize(step * 20.0 + 1.0)  # zmena velikosti vykreslovanych bodu
        glBegin(GL_POINTS)
        glVertex2f(50.0 + 300.0 * step, 150.0)
        glEnd()


# spuštění smyčky pro zpracování událostí
pyglet.app.run()
