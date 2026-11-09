dicts = [{"foo": 1}, {"bar": 2}, {"baz": 3}, {"foo": 4}]

x = {k: v for D in dicts for k,v in D.items()}

for key, value in x.items():
    print(key, value)
