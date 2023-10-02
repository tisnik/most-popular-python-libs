from funcy import reraise

class MathException(Exception):
    def __init__(self, message):
        self.message = message


@reraise(errors=Exception, into=lambda e: MathException("neděl nulou! " + str(e)))
def divide(a, b):
    return a/b


print(divide(1, 2))
print(divide(1, 0))
