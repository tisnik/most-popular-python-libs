from cffi import FFI

ffi = FFI()

ffi.cdef("""
    void swap(int *x, int *y);
""")

def load_library(library_name):
    return ffi.dlopen(library_name)


swapper = load_library("libswapper.so")

x = ffi.new("int *", 10)
y = ffi.new("int *", 20)

swapper.swap(x, y)
print(x[1])
print(y[1])
