#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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
from PIL import ImageOps

filename = "Lenna.png"

try:
    test_image = Image.open(filename)
    test_image.load()
    modified_image_1 = ImageOps.autocontrast(test_image, cutoff=0)
    modified_image_2 = ImageOps.autocontrast(test_image, cutoff=50)
    modified_image_3 = ImageOps.autocontrast(test_image, cutoff=75)

    test_image.show()
    modified_image_1.show()
    modified_image_2.show()
    modified_image_3.show()

except Exception as e:
    print(e)
