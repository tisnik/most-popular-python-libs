from mpmath import mpf

x = mpf("1.23e10000000")
y = 42

z = x + y
print(type(z))
print(z)

w = y + x
print(type(w))
print(w)
