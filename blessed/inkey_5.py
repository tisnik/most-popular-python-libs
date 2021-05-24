import blessed

terminal = blessed.Terminal()

with terminal.raw():
    while True:
        key = terminal.inkey()
        if key == 'q':
            break
        print(key)
