#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2023  Pavel Tisnovsky
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
# https://tisnik.github.io/most-popular-python-libs/asizeof/asizeof02.html
# 
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/asizeof/asizeof02.html

from pympler import asizeof

for item in dir(asizeof):
    if item[0] != "_":
        print(item)
