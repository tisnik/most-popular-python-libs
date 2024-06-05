# Compiled Coconut: -----------------------------------------------------------

print((isinstance)("hello", str))  #1 (line in Coconut source)

factorial = lambda n: reduce(lambda a, b: a * b, range(1, n + 1), 1)  #3 (line in Coconut source)

def nad(n, k):  #5 (line in Coconut source)
    return factorial(n) / (factorial(k) * factorial(n - k))  #6 (line in Coconut source)


for k in range(5):  #8 (line in Coconut source)
    (print)((nad)(4, k))  #9 (line in Coconut source)
