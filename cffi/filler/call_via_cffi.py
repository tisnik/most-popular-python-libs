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

from cffi import FFI

ffi = FFI()

ffi.cdef("""
    void fill(int *x, int, int);
""")

def load_library(library_name):
    return ffi.dlopen(library_name)


filler = load_library("libfiller.so")

array = ffi.new("int[10]")
print(list(array))

filler.fill(array, len(array)//2, 42)
print(list(array))

filler.fill(array+5, len(array)//2, -1)
print(list(array))
