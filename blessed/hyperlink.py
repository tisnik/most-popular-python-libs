"""Displays active hyperlink on terminal."""

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

# display text containing active hyperlink (on most terminals)
print(f"Odkaz: {terminal.link('https://www.root.cz', 'Stránky Root.cz')}")
