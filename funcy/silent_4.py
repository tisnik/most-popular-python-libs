from funcy import silent

@silent
def cat(filename):
    with open(filename) as fin:
        print(fin.read())


cat("silent_3.py")
cat("this_does_not_exists")
