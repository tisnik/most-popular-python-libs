# Simplified version of Coconut transpiled into Python

def swap(x, y):
    return y, x



def sub(x, y):
    return x - y



print(*(1, 2))
print(sub(*(1, 2)))
print(sub(*swap(*(1, 2))))
