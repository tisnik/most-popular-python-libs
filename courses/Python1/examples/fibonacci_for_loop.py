def fibonacci(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


for n in range(0, 21):
    print(n, fibonacci(n))
