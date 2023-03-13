from guppy import hpy

for item in dir(hpy()):
    if item[0] != "_":
        print(item)
