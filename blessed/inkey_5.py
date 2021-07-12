"""Keyboard input handling in Blessed library."""

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

# enter raw mode
with terminal.raw():
    while True:
        # read one key
        key = terminal.inkey()
        if key == 'q':
            break

        # display key
        print(key)
