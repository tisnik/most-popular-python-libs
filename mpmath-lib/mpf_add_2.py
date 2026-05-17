from mpmath import mpf

x = mpf("1.00")
y = 2.0

z = x + y
print(type(z))
print(z)

w = y + x
print(type(w))
print(w)
