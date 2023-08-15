from funcy import compose


composed = compose(len, str)

print(composed)
print(composed(0))
print(composed(42))
print(composed(1000))
