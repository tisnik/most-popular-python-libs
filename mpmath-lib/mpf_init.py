from mpmath import mpf

# výchozí hodnota
a = mpf()
print(type(a))
print(a)

# získání hodnoty z řetězce
b = mpf("1.23456")
print(type(b))
print(b)

# získání hodnoty z typu float
c = mpf(1.23456)
print(type(c))
print(c)

# získání hodnoty z typu int
d = mpf(42)
print(type(d))
print(d)
