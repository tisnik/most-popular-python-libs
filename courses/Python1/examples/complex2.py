class Complex:
    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)


c1 = Complex(1, 2)
c2 = Complex(10, 20)
c3 = Complex(100)
c4 = Complex()

c5 = Complex(1, 2)
print(c1)
print(c2)
print(c3)
print(c4)
