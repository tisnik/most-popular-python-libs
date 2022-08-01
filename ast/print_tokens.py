import token

for name, value in vars(token).items():
    if not name.startswith('_'):
        if isinstance(value, int):
            print("{:20s} {}".format(name, value))
