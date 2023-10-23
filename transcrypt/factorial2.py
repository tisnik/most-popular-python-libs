def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    assert isinstance(n, int), "Integer expected"

    if n < 0:
        raise ValueError(n)
    if n == 0:
        return 1
    result = n * factorial(n - 1)

    assert isinstance(result, int), "Internal error in factorial computation"
    return result


def main():
    for n in range(0, 11):
        print(n, factorial(n))
    print(factorial(-1))


if __name__ == "__main__":
    main()
