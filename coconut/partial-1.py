# Compiled Coconut: -----------------------------------------------------------

def mul(x, y):  #1 (line in Coconut source)
    return x * y  #2 (line in Coconut source)



print(mul(6, 7))  #5 (line in Coconut source)

print()  #7 (line in Coconut source)

doubler = _coconut_partial(mul, 2)  #9 (line in Coconut source)


for i in range(11):  #12 (line in Coconut source)
    print(i, doubler(i))  #13 (line in Coconut source)
