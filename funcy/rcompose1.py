from funcy import rcompose


composed = rcompose(str, len)

print(composed)
print(composed(0))
print(composed(42))
print(composed(1000))
