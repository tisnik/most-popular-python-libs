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
greeter = load_library("libgreeter.so")
greeter.greet("world".encode("utf-8"))
