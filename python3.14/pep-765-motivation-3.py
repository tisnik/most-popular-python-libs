def test_fn():
    for x in range(10):
        try:
            y = 1 / x
            print(f"{x:2}  {y:4.2f}")
        except ZeroDivisionError:
            print(f"{x:2}  divide by zero")
        finally:
            return


test_fn()
