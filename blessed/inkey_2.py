import blessed

terminal = blessed.Terminal()

with terminal.cbreak():
    while True:
        key = terminal.inkey()
        print(key.name, key.code, key)
