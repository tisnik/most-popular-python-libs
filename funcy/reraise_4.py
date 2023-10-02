from funcy import reraise

class MathException(Exception):
    def __init__(self, message):
        self.message = message


@reraise(errors=[], into=MathException("neděl nulou!"))
def divide(a, b):
    return a/b


print(divide(1, 2))
print(divide(1, 0))
