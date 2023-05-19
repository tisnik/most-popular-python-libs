from numba import jit


@jit(nopython=True,nogil=True)
def sum(a, b):
     return a+b


x = sum(1, 2)
y = sum(1.1, 2.2)
z = sum((1, 2), (3, 4))

print(x)
print(y)
print(z)
