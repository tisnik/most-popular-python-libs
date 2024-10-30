from functools import reduce


def factorial(n):
    """Výpočet faktoriálu pomocí reduce."""
    return reduce(lambda a, b: a * b, range(1, n + 1))


# výpočet 10!
print(factorial(10))

# tabulka s hodnotami n!
for n in range(1, 11):
    print(n, factorial(n))
