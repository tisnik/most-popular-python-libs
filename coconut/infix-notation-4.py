# Compiled Coconut: -----------------------------------------------------------

def add(a, b):  #1 (line in Coconut source)
    return a + b  #2 (line in Coconut source)


def mul(x, y):  #4 (line in Coconut source)
    return x * y  #5 (line in Coconut source)


(print)((mul)((add)(1, 2), 3))  #7 (line in Coconut source)
(print)((add)(1, ((mul)(2, 3))))  #8 (line in Coconut source)
