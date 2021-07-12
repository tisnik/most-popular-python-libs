"""Usage of move_xy method."""

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import blessed

# initialize terminal
terminal = blessed.Terminal()

# enter cbreak mode (rare mode)
with terminal.cbreak():
    # display part of frame using move_xy command
    for x in range(terminal.width):
        print(f"{terminal.move_xy(x, 0)}-", end="", flush=True)
        print(f"{terminal.move_xy(x, terminal.height-1)}-", end="", flush=True)

    # display part of frame using move_xy command
    for y in range(terminal.height-1):
        print(f"{terminal.move_xy(0, y)}|", end="", flush=True)
        print(f"{terminal.move_xy(terminal.width-1, y)}|", end="", flush=True)

    # display centered text
    with terminal.location(y=terminal.height // 2):
        print(terminal.center(terminal.bold("Press any key to exit...")))

    # wait for key
    terminal.inkey()
