sets = [{"foo"}, {"bar", "baz"}, {"x", "y", "z"}]

x = {x for S in sets for x in S}

for i, item in enumerate(x):
    print(i, item)
