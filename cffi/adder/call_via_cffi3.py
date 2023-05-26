from cffi import FFI

ffi = FFI()

ffi.cdef("""
    int add(int x, int y);
""")

def load_library(library_name):
    return ffi.dlopen(library_name)


adder = load_library("libadder.so")
print(adder.add(1,2**100))
