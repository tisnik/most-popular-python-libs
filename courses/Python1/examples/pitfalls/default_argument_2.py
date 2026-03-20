# výchozí hodnota funkce je vyhodnocena pouze jedenkrát
# a to ve chvíli definici funkce


def foo(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar


print(foo())

print(foo())

print(foo())
