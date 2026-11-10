sets = [{"foo", "bar"}, {"bar", "baz"}, {"foo", "baz"}]

x = {*S for S in sets}

for i, item in enumerate(x):
    print(i, item)
