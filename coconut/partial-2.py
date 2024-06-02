# Compiled Coconut: -----------------------------------------------------------

def mul(x, y, z):  #1 (line in Coconut source)
    return x * y * z  #2 (line in Coconut source)



print(mul(2, 3, 7))  #5 (line in Coconut source)

print()  #7 (line in Coconut source)

doubler = _coconut_partial(mul, 2)  #9 (line in Coconut source)


for i in range(11):  #12 (line in Coconut source)
    print(i, doubler(i, 10))  #13 (line in Coconut source)
