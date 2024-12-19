"""Uložení řetězce do sekvence bajtů s volitelných kódováním."""

s = "The quick brown fox jumps over the lazy dog"

x = bytes(s, "ascii")
print(type(x))
print(x)
print()

y = bytes(s, "utf-8")
print(type(y))
print(y)
print()

z = bytes(s, "utf-16-le")
print(type(z))
print(z)
print()

w = bytes(s, "utf-16-be")
print(type(w))
print(w)
print()

# UTF-8 s BOM, pouziva ho napriklad Notepad a dalsi divne aplikace
q = bytes(s, "utf-8-sig")
print(type(q))
print(q)
print()

