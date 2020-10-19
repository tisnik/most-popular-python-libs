#!/usr/bin/env python
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
from PIL import ImageMath
from PIL import ImageStat

filename = "Lenna.png"

try:
    # načtení originálního obrázku Leny
    test_image = Image.open(filename)
    test_image.load()

    # převod na černobílý obrázek
    modified_image = ImageMath.eval("convert(src, '1')", src=test_image)

    # inicializace třídy se statistikami o obrázku
    stat = ImageStat.Stat(modified_image)

    # zobrazení statistických informací o obrázku
    print("Pixel count:          {cnt}".format(cnt=stat.count))
    print("Min value:            {min}".format(min=[v[0] for v in stat.extrema]))
    print("Max value:            {max}".format(max=[v[1] for v in stat.extrema]))
    print("Average value:        {val}".format(val=stat.mean))
    print("Median value:         {med}".format(med=stat.median))
    print("Variance:             {var}".format(var=stat.var))
    print("Std.deviation value:  {stddev}".format(stddev=stat.stddev))

except Exception as e:
    print(e)
