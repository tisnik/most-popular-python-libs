from mpmath import mpf

def factorial(n):
    """Výpočet faktoriálu ve smyčce."""
    f = mpf("1")
    for x in range(1, n + 1):
        f *= x
    return f


for n in range(31):
    print(n, factorial(n))
