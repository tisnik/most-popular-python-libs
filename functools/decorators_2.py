def wrapper1(function):
    def inner_function():
        print("-" * 40)
        function()
        print("-" * 40)

    return inner_function


@wrapper1
def hello():
    print("Hello!")


hello()
