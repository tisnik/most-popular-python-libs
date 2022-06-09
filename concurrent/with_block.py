class Context:
    def __init__(self):
        print("Context: init")

    def __enter__(self):
        print("Context: enter")
        return "foo"

    def __exit__(self, type, value, traceback):
        print("Context: exit", type, value, traceback)


print("Before with block")

with Context() as c:
    print("Inside with block")
    print(c)

print("After with block")
