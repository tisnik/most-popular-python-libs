seznam = []


def foo(x):
    seznam.append(x)


print(seznam)
foo(1)
print(seznam)
foo(2)
print(seznam)


def bar(x):
    global seznam
    seznam += [x]


print(seznam)
bar(3)
print(seznam)
bar(4)
print(seznam)
