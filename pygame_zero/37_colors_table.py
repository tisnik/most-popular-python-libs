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

from pygame.colordict import THECOLORS

for i, color in enumerate(sorted(THECOLORS)):
    if i % 5 == 0:
        print("<tr>", end="")
    print("<td>" + color + "</td>", end="")
    if i % 5 == 4:
        print("</tr>")
