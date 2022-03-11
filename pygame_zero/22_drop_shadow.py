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
    screen.fill("gray")

    screen.draw.text(
        "Pygame Zero",
        (140, HEIGHT / 2 - 20),
        fontsize=40,
        shadow=(1, 1),
        scolor="#202020",
        color="white",
    )
