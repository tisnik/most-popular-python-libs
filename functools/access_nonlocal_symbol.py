def foo():
    message = "FOO-BAR"

    def bar():
        print(message)
    return bar

x = foo()
x()
