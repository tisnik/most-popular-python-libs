def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    return 1 if n <= 1 else n * factorial(n - 1)


# výpočet 10!
print(factorial(10))

# tabulka s hodnotami n!
for n in range(1, 11):
    print(n, factorial(n))
