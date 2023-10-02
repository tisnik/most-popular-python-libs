from funcy import ignore

@ignore(errors=Exception)
def divide(a, b):
    return a/b


print(divide(1, 2))
print(divide(1, 0))
