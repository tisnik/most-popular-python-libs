import pathlib

from cffi import FFI

ffi = FFI()

def load_header(filename):
    directory = pathlib.Path().absolute()
    header = directory / filename
    with open(header) as fin:
        return fin.read()


def load_library(library_name):
    return ffi.dlopen(library_name)


ffi.cdef(load_header("array_printer.h"))

rows = 20

array = ffi.new("float [][3]", rows)

array[0] = (1,2,3)
array[rows//2] = (4,5,6)
array[rows-1] = (7,8,9)

printer = load_library("libaprinter.so")
printer.print_array(array, rows)
