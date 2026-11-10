lists = [["foo"], ["bar", "baz"], ["x", "y", "z"]]

x = [item for L in lists for item in L]

for i, item in enumerate(x):
    print(i, item)
