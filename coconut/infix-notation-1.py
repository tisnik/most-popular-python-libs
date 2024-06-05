# Compiled Coconut: -----------------------------------------------------------

def add(a, b):  #1 (line in Coconut source)
    return a + b  #2 (line in Coconut source)


print(add(1, 2))  #4 (line in Coconut source)
print((add)(1, 2))  #5 (line in Coconut source)

(print)((add)(1, 2))  #7 (line in Coconut source)
