"""Retrieve test image, resize it, and store under new filename."""

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

from PIL import Image
import urllib.request

url = "https://homepages.cae.wisc.edu/~ece533/images/fruits.png"

original_filename = "fruits_.png"
resized_filename = "fruits.png"

urllib.request.urlretrieve(url, original_filename)

img = Image.open(original_filename)
resized = img.resize((128, 128), Image.BILINEAR)
resized.save(resized_filename)
