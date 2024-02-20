from toolz.itertoolz import join

names = [
    (0, "Alice"),
    (1, "Bob"),
    (2, "Charlie"),
]

phones = [
    ("Alice",   "555-1234"),
    ("Bob",     "555-5678"),
    ("Charlie", "555-9999"),
]

for item in join(1, names, 0, phones): 
    print(item[0][0], item[0][1], item[1][1])
