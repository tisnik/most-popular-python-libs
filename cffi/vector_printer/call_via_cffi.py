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


ffi.cdef(load_header("vector_printer.h"))

vector = ffi.new("vector_t *")
vector.x = 1
vector.y = 2
vector.z = 3

vprinter = load_library("libvprinter.so")
vprinter.print_vector(vector[0])
