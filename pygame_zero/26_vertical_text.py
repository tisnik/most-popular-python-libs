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
    screen.fill("black")

    screen.draw.text(
        "Pygame Zero",
        (WIDTH / 2 - 20, HEIGHT - 60),
        angle=90,
        fontsize=80,
        color="orange",
        gcolor="red",
    )
