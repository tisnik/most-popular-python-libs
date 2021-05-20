"""Výpočet faktoriálu."""

def factorial(n):
    if n is None:
        return None
    if n < 0:
        return None
    if n == 0:
        return 1

    r = factorial(n-1)

    if r is None:
        return None
    return n * r
