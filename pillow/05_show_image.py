#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Nacteni a zobrazeni rastroveho obrazku."""

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

from PIL import Image

FILENAME = "Lenna.png"

try:
    test_image = Image.open(FILENAME)
    test_image.load()
    test_image.show()

except Exception as e:
    print(e)
