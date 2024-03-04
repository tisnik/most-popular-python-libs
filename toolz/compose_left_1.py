from toolz import compose_left


composed = compose_left(str, len)

print(composed)
print(composed(0))
print(composed(42))
print(composed(1000))
