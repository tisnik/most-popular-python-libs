from cffi import FFI

ffi = FFI()

ffi.cdef("""
    void fill(int *x, int, int);
""")

def load_library(library_name):
    return ffi.dlopen(library_name)


filler = load_library("libfiller.so")

array = ffi.new("int[10]")
print(list(array))

filler.fill(array, len(array)//2, 42)
print(list(array))

filler.fill(array+5, len(array)//2, -1)
print(list(array))
