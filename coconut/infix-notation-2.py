# Compiled Coconut: -----------------------------------------------------------

print((isinstance)("hello", str))  #1 (line in Coconut source)

@_coconut_tco  #3 (line in Coconut source)
def factorial(n):  #3 (line in Coconut source)
    if n <= 1:  #4 (line in Coconut source)
        return 1  #5 (line in Coconut source)
    else:  #6 (line in Coconut source)
        return _coconut_tail_call((reduce), _coconut.operator.mul, range(1, n + 1))  #7 (line in Coconut source)


def choose(n, k):  #9 (line in Coconut source)
    return factorial(n) / (factorial(k) * factorial(n - k))  #10 (line in Coconut source)


print(factorial(10))  #12 (line in Coconut source)

for k in range(5):  #14 (line in Coconut source)
    print(choose(4, k))  #15 (line in Coconut source)

print()  #17 (line in Coconut source)

for k in range(5):  #19 (line in Coconut source)
    print((choose)(4, k))  #20 (line in Coconut source)

def nad(n, k):  #22 (line in Coconut source)
    return factorial(n) / (factorial(k) * factorial(n - k))  #23 (line in Coconut source)


print()  #25 (line in Coconut source)

for k in range(5):  #27 (line in Coconut source)
    print((nad)(4, k))  #28 (line in Coconut source)
