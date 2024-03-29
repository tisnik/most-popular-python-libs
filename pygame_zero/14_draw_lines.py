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

BORDER = 20


def draw():
    screen.fill("white")

    for i in range(0, WIDTH - BORDER + 1, 10):
        color = i * 255 / WIDTH
        screen.draw.line(
            (BORDER, i), (BORDER + i, HEIGHT - BORDER), (color, 0, 255 - color)
        )
