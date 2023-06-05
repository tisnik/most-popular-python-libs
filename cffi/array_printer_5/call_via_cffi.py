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

array = ffi.new("vector_t[10]")

for i in range(len(array)):
    array[i].x = i
    array[i].y = 2*i
    array[i].z = 1 / (1+i)

printer = load_library("libaprinter.so")
printer.print_array(array, len(array))
