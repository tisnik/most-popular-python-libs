sets = [{"foo"}, {"bar", "baz"}, {"x", "y", "z"}]

x = {*S for S in sets}

for i, item in enumerate(x):
    print(i, item)
