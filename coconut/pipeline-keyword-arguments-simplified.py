# Simplified version of Coconut transpiled into Python

def swap(x=0, y=0):
    return y, x



def sub(x, y):
    return x - y



params = _coconut.dict((("x", 1), ("y", 2)))
print(sub(*swap(**params)))

params = _coconut.dict((("y", 2), ("x", 1)))
print(sub(*swap(**params)))
