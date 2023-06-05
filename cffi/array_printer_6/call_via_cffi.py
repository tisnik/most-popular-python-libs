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

array = ffi.new("float [10][3]")

array[0] = (1,2,3)
array[5] = (4,5,6)
array[9] = (7,8,9)

printer = load_library("libaprinter.so")
printer.print_array(array, 10)
