try:
    with open("pep-758-motivation.py", "r") as fin:
        content = fin.read()
    with open("bar", "w") as fout:
        fout.write(content)
except FileNotFoundError, PermissionError, IsADirectoryError, IOError as e:
    print(type(e))
