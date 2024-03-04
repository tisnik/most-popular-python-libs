from toolz import curry


def hello():
    print("Hello, world!")


curried = curry(hello)
print(hello)
print(curried)
curried()
