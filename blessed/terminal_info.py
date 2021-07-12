"""Retrieving basic terminal info."""

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

# display basic information about terminal
print("Resolution: {}x{} characters".format(terminal.width, terminal.height))
print("Number of colors: {}".format(terminal.number_of_colors))
