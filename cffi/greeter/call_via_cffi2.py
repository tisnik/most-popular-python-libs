from cffi import FFI

ffi = FFI()

ffi.cdef("""
    void greet(char *x);
""")

def load_library(library_name):
    return ffi.dlopen(library_name)


greeter = load_library("libgreeter.so")
greeter.greet(b"world")
