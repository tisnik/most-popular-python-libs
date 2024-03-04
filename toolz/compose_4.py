from toolz import compose


composed = compose(
        lambda x: -x if x<0 else x,
        lambda x: x*2,
        lambda x, y: x+y)

print(composed(2, 3))
print(composed(-2, -3))
