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
    screen.fill("darkgreen")
    center = WIDTH // 2, WIDTH // 2
    radius = WIDTH // 3
    screen.draw.circle(center, radius, (255, 255, 255))
