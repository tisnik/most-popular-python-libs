from funcy import silent

@silent
def raise_exception():
    raise Exception("foo")


raise_exception()
