# Compiled Coconut: -----------------------------------------------------------

def swap(x, y):  #1 (line in Coconut source)
    return y, x  #2 (line in Coconut source)



def sub(x, y):  #5 (line in Coconut source)
    return x - y  #6 (line in Coconut source)



(print)(*(1, 2))  #9 (line in Coconut source)
(print)((sub)(*(1, 2)))  #10 (line in Coconut source)
(print)((sub)(*(swap)(*(1, 2))))  #11 (line in Coconut source)
