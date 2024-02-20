from toolz.itertoolz import get

phonebook = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9999"}

print(get("Bob", phonebook))
print(get(["Alice", "Bob"], phonebook))
print(get("Zdenek", phonebook, "unknown"))
print(get("Zdenek", phonebook))
