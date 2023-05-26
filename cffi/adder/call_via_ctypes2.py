import ctypes


def load_library(library_name):
    return ctypes.CDLL(library_name)


adder = load_library("libadder.so")
print(adder.add(1,"foo"))
