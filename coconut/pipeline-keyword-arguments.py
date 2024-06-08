# Compiled Coconut: -----------------------------------------------------------

def swap(x=0, y=0):  #1 (line in Coconut source)
    return y, x  #2 (line in Coconut source)



def sub(x, y):  #5 (line in Coconut source)
    return x - y  #6 (line in Coconut source)



params = _coconut.dict((("x", 1), ("y", 2)))  #9 (line in Coconut source)
(print)((sub)(*(swap)(**params)))  #13 (line in Coconut source)

params = _coconut.dict((("y", 2), ("x", 1)))  #15 (line in Coconut source)
(print)((sub)(*(swap)(**params)))  #19 (line in Coconut source)
