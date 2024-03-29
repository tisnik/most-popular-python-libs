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


def draw():
    screen.fill("white")

    angles = range(0, 360, 45)
    colors = ("red", "orange", "yellow", "green", "blue", "#4B0082", "violet", "gray")

    for angle, color in zip(angles, colors):
        screen.draw.text(
            "  colors", (WIDTH / 2, HEIGHT / 2), angle=angle, fontsize=80, color=color
        )
