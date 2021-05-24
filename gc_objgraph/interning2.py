import sys

last_letter = "d"

a = sys.intern("Hello World")
b = sys.intern("Hello Worl" + last_letter)

print("The ID of a: {}".format(id(a)))
print("The ID of b: {}".format(id(b)))
print("a is b? {}".format(a is b))
