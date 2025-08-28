# Knihovna PySimpleGUI
#
# - otevření jednoduchého okna bez dalších ovládacích prvků

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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/01-empty-window.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/01-empty-window.html

import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [[]]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #1", layout, size=(320, 240))

# čekání na událost
window.read()

# po vzniku událostí aplikaci ukončíme
window.close()
