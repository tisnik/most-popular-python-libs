dicts = [{"foo": 1}, {"bar": 2}, {"baz": 3}, {"foo": 4}]

x = {**D for D in dicts}

for key, value in x.items():
    print(key, value)
