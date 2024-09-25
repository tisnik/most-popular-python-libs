def factorial(n):
    """Výpočet faktoriálu ve smyčce."""
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f
