# Compiled Coconut: -----------------------------------------------------------

factorial = lambda n: reduce(lambda a, b: a * b, range(1, n + 1), 1)  #1 (line in Coconut source)


for n in range(0, 11):  #4 (line in Coconut source)
    print(n, factorial(n))  #5 (line in Coconut source)
