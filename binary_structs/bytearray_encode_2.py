s = "ěščřžýáíéů"

# nelze převést na čisté ASCII
# x = bytearray(s, "ascii")
# print(type(x))
# print(x)
# print()

y = bytearray(s, "utf-8")
print(type(y))
print(y)
print()

z = bytearray(s, "utf-16-le")
print(type(z))
print(z)
print()

w = bytearray(s, "utf-16-be")
print(type(w))
print(w)
print()

# UTF-8 s BOM, pouziva ho napriklad Notepad a dalsi divne aplikace
q = bytearray(s, "utf-8-sig")
print(type(q))
print(q)
print()

