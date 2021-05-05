import blessed

terminal = blessed.Terminal()

with terminal.cbreak():
    while True:
        key = terminal.inkey(timeout=0.3)

        if str(key) == "":
            print("Nothing... try again")
        elif key.is_sequence:
            print("got sequence: {0}.".format(key.name, key.code, (str(key))))
        else:
            print(key.name, key.code, key)
