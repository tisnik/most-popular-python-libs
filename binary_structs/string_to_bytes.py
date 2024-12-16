s = "The quick brown fox jumps over the lazy dog"

x = s.encode("ascii")
print(type(x))
print(x)
print()

y = s.encode("utf-8")
print(type(y))
print(y)
print()

z = s.encode("utf-16-le")
print(type(z))
print(z)
print()

w = s.encode("utf-16-be")
print(type(w))
print(w)
print()

q = s.encode("utf-8-sig")
print(type(q))
print(q)
print()

