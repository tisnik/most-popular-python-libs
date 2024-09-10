#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Nacteni rastroveho obrazku knihovnou Pillow."""

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

test_image = Image.open(FILENAME)
test_image.load()
print(test_image)
