class Foo:
    def __init__(self):
        self._enabled = False

    def set_enabled(self, state):
        self._enabled = state

    def __str__(self):
        return "Foo that is " + ("enabled" if self._enabled else "disabled")


foo = Foo()
print(foo)

foo.set_enabled(True)
print(foo)

foo.set_enabled(False)
print(foo)
