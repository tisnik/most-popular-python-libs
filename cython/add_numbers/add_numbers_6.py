import cython

@cython.cfunc
@cython.nogil
def add_two_numbers(x: cython.int, y: cython.int) -> cython.int:
    print(x)
    return x + y


z = add_two_numbers(123, 456)
print(z)
