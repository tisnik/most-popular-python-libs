from toolz.itertoolz import pluck

phonebook = [
    {"id": 0, "name": "Alice", "phone": "555-1234"},
    {"id": 1, "name": "Bob", "phone": "555-5678"},
    {"id": 2, "name": "Charlie", "phone": "555-9999"},
]

print(list(pluck(["name", "phone"], phonebook)))
