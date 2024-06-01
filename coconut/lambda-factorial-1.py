# Compiled Coconut: -----------------------------------------------------------

@_coconut_tco  #1 (line in Coconut source)
def factorial(n):  #1 (line in Coconut source)
    return _coconut_tail_call(reduce, a, lambda b: a * b, range(1, n + 1), 1)  #2 (line in Coconut source)



for n in range(0, 11):  #5 (line in Coconut source)
    print(n, factorial(n))  #6 (line in Coconut source)
