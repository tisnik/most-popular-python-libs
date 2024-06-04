# Compiled Coconut: -----------------------------------------------------------

double = _coconut_partial(fmap, lambda x: x * 2)  #1 (line in Coconut source)

print(double([1, 2, 3, 4]))  #3 (line in Coconut source)
print(double((1, 2, 3, 4)))  #4 (line in Coconut source)
print(double(range(10)))  #5 (line in Coconut source)
