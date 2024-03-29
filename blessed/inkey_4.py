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

# enter cbreak mode (rare mode)
with terminal.cbreak():
    while True:
        # read one key with specified timeout
        key = terminal.inkey(timeout=0.3)

        # display key or sequence
        if str(key) == "":
            print("Nothing... try again")
        elif key.is_sequence:
            print("got sequence: {0} {1} {2}.".format(key.name, key.code, (str(key))))
        else:
            print(key.name, key.code, key)
