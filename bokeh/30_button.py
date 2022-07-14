#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# naimportujeme vybrané funkce z knihovny `bokeh.io`
from bokeh.io import show

# naimportujeme vybrané funkce z knihovny `bokeh.models`
from bokeh.models import Button, CustomJS

# vytvoření ovládacího prvku
button = Button(label="Foo", button_type="success")

# specifikace handleru
button.js_on_click(CustomJS(code="console.log('button: click!', this.toString())"))

# zobrazení ovládacího prvku
show(button)
