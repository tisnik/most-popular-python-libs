from funcy import ignore

@ignore(errors=ZeroDivisionError)
def divide(a, b):
    return a/b


print(divide(1, 2))
print(divide(1, 0))
