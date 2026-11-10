lists = [["foo"], ["bar", "baz"], ["x", "y", "z"]]

x = [L for L in lists]

for i, item in enumerate(x):
    print(i, item)
