for i in range(-10, 11):
    try:
        f = factorial(i)
        print(f"{i}! = {f}")
    except ValueError as e:
        print(f"{i}! nelze vypocitat:", e)
