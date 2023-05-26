import ctypes


def load_library(library_name):
    return ctypes.CDLL(library_name)


greeter = load_library("libgreeter.so")
greeter.greet("world".encode("utf-8"))
