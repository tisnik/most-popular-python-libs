class Complex:
    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag

    def __str__(self):
        return "{r} + {i}j".format(r=self._real, i=self._imag)

    def __eq__(self, other):
        """Přetížení binárního operátoru ==."""
        return self._real == other._real and self._imag == other._imag

    def __neg__(self):
        """Přetížení unárního operátoru -."""
        return Complex(-self._real, -self._imag)

    def __add__(self, other):
        """Přetížení binárního operátoru +."""
        r = self._real + other._real
        i = self._imag + other._imag
        return Complex(r, i)

    def __sub__(self, other):
        """Přetížení binárního operátoru -."""
        r = self._real - other._real
        i = self._imag - other._imag
        return Complex(r, i)

    def __iadd__(self, other):
        """Přetížení binárního operátoru +=."""
        self._real += other._real
        self._imag += other._imag
        return self


c1 = Complex(1, 2)
c2 = Complex(10, 20)
c3 = Complex(100)
c4 = Complex()

print("c1:", c1)
print("c2:", c2)
print("c3:", c3)
print("c4:", c4)

print()

print("-c1:", -c1)
print("-c2:", -c2)

print()

print("c1 + c2:", c1+c2)
print("c1 + c3:", c1+c3)
print("c1 - c2:", c1-c2)
print("c1 - c3:", c1-c3)

c2 += c3
print("c2 += c3:", c1)

print()

c5 = Complex(1, 2)
print("c1 == c5:", c1 == c5)
print("c2 == c5:", c2 == c5)
print("c3 == c5:", c3 == c5)
