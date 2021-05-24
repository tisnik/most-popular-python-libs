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
from PIL import ImageStat

filename = "Lenna.png"

try:
    # načtení originálního obrázku Leny
    test_image = Image.open(filename)
    test_image.load()

    # inicializace třídy se statistikami o obrázku
    stat = ImageStat.Stat(test_image)

    # zobrazení statistických informací o obrázku
    print("Pixel count:           {cnt}".format(cnt=stat.count))
    print("Min values:            {min}".format(min=[v[0] for v in stat.extrema]))
    print("Max values:            {max}".format(max=[v[1] for v in stat.extrema]))
    print("Average values:        {val}".format(val=stat.mean))
    print("Median values:         {med}".format(med=stat.median))
    print("Variance:              {var}".format(var=stat.var))
    print("Std.deviation values:  {stddev}".format(stddev=stat.stddev))

except Exception as e:
    print(e)
