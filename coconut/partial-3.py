# Compiled Coconut: -----------------------------------------------------------

def mul(x, y, z, w):  #1 (line in Coconut source)
    return x * y * z * w  #2 (line in Coconut source)



f1 = mul  #5 (line in Coconut source)
print(f1)  #6 (line in Coconut source)

f2 = _coconut_partial(f1, 2)  #8 (line in Coconut source)
print(f2)  #9 (line in Coconut source)

f3 = _coconut_partial(f2, 3)  #11 (line in Coconut source)
print(f3)  #12 (line in Coconut source)

f4 = _coconut_partial(f3, 4)  #14 (line in Coconut source)
print(f4)  #15 (line in Coconut source)

f5 = _coconut_partial(f4, 5)  #17 (line in Coconut source)
print(f5)  #18 (line in Coconut source)

f6 = _coconut_partial(f5, 6)  #20 (line in Coconut source)
print(f6)  #21 (line in Coconut source)

print()  #23 (line in Coconut source)

print(f1(2, 3, 4, 5))  #25 (line in Coconut source)
print(f2(3, 4, 5))  #26 (line in Coconut source)
print(f3(4, 5))  #27 (line in Coconut source)
print(f4(5))  #28 (line in Coconut source)
print(f5())  #29 (line in Coconut source)
print(f6())  #30 (line in Coconut source)
