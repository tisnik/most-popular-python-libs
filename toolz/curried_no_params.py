from toolz import curry


@curry
def hello():
    print("Hello, world!")


print(hello)
hello()
