# výchozí hodnota funkce je vyhodnocena pouze jedenkrát
# a to ve chvíli definici funkce


def foo(bar=[]):
    bar.append("baz")
    return bar


print(foo())

print(foo())

print(foo())
