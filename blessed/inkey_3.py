import blessed

terminal = blessed.Terminal()

with terminal.cbreak():
    while True:
        key = terminal.inkey()
        if key.is_sequence:
            print("got sequence: {0}.".format(key.name, key.code, (str(key))))
        else:
            print(key.name, key.code, key)
