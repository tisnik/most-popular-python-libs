def wrapper1(function):
    def inner_function():
        print("-" * 40)
        function()
        print("-" * 40)

    return inner_function


def wrapper2(function):
    def inner_function():
        print("=" * 40)
        function()
        print("=" * 40)

    return inner_function


@wrapper1
@wrapper2
def hello():
    print("Hello!")


hello()
