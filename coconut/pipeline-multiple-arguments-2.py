# Compiled Coconut: -----------------------------------------------------------

def swap(x, y):  #1 (line in Coconut source)
    return y, x  #2 (line in Coconut source)



(print)(*(1, 2))  #5 (line in Coconut source)
(print)(((_coconut_minus))(*(1, 2)))  #6 (line in Coconut source)
(print)(((_coconut_minus))(*(swap)(*(1, 2))))  #7 (line in Coconut source)
