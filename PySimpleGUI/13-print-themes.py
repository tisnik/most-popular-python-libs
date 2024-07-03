#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#
#
# link to source:
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/13-print-themes.py
# 
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/13-print-themes.html

import PySimpleGUI as sg

themes = sorted(sg.LOOK_AND_FEEL_TABLE.keys())

print("\n".join(themes))
