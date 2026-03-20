def factorial(n):
    """Výpočet faktoriálu ve smyčce."""
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f


# výpočet 10!
print(factorial(10))

# tabulka s hodnotami n!
for n in range(1, 11):
    print(n, factorial(n))
