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

BORDER = 60


def draw():
    screen.fill("white")

    message = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed"
               "viverra vestibulum eros at pulvinar. Phasellus vitae mattis nibh. Cras et"
               "turpis ac erat eleifend lobortis a at ante. Nulla tincidunt quis sapien"
               "vitae ultricies. Curabitur suscipit bibendum lectus, at ornare elit finibus"
               "vel. Nullam aliquet libero vitae mattis mattis. Praesent id libero tempor,"
               "finibus metus a, fermentum velit.")

    screen.draw.text(message,
                     (BORDER, 100),
                     width=WIDTH - BORDER*2,
                     fontname="freesans",
                     fontsize=20,
                     color="navy")
