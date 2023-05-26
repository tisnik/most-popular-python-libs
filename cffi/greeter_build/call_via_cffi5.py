import pathlib

from cffi import FFI

ffi = FFI()


def load_header(filename):
    directory = pathlib.Path().absolute()
    header = directory / "greeter.h"
    with open(header) as fin:
        return fin.read()


def load_library(library_name):
    return ffi.dlopen(library_name)


ffi.cdef(load_header("greeter.h"))

ffi.set_source(
    "_greeter",
    '#include "greeter.h"',
    sources=["greeter.c"],
)

ffi.compile(verbose=True)

from _greeter import ffi, lib
lib.greet("world".encode("utf-8"))
