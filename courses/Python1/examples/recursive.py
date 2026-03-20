def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial(10))

for n in range(1, 11):
    print(n, factorial(n))
