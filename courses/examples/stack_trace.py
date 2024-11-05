def factorial(n):
    if n < 0:
        raise ValueError("factorial ocekava kladne parametry, bylo predano", n)
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n*factorial(n-1)


def funkce1(n):
    return factorial(n)


def funkce2(n):
    return funkce1(n)


def funkce3(n):
    return funkce2(n)


funkce3(-10)
