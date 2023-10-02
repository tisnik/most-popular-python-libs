from funcy import silent

@silent
def call_function_to_raise_exception():
    raise_exception()


def raise_exception():
    raise Exception("foo")


call_function_to_raise_exception()
