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
    screen.draw.line((BORDER, BORDER), (WIDTH-BORDER, BORDER), (255, 255, 255))
    screen.draw.line((WIDTH-BORDER, BORDER), (WIDTH-BORDER, HEIGHT-BORDER), (255, 255, 255))
    screen.draw.line((BORDER, BORDER), (BORDER, HEIGHT-BORDER), (255, 255, 255))
    screen.draw.line((BORDER, HEIGHT-BORDER), (WIDTH-BORDER, HEIGHT-BORDER), (255, 255, 255))
