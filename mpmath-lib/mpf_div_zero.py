from mpmath import mpf

one = mpf("1")
zero = mpf("0")

try:
    x = one/zero
except Exception as e:
    print(type(e))

try:
    x = -one/zero
except Exception as e:
    print(type(e))

try:
    x = zero/zero
except Exception as e:
    print(type(e))
