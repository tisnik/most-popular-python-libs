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

terminal = blessed.Terminal()

with terminal.cbreak():
    while True:
        key = terminal.inkey()
        if key.is_sequence:
            print("got sequence: {0}.".format(key.name, key.code, (str(key))))
        else:
            print(key.name, key.code, key)
