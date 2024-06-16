def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    if n < 0:
        return None
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    return result
