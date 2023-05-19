from numba import jit


@jit(nopython=True,nogil=True)
def sum(a, b):
     return a+b


x = sum(1, 2)
print(x)
