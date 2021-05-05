import blessed

terminal = blessed.Terminal()

with terminal.cbreak():
    for x in range(terminal.width):
        print(f"{terminal.move_xy(x, 0)}-", end="", flush=True)
        print(f"{terminal.move_xy(x, terminal.height-1)}-", end="", flush=True)

    for y in range(terminal.height-1):
        print(f"{terminal.move_xy(0, y)}|", end="", flush=True)
        print(f"{terminal.move_xy(terminal.width-1, y)}|", end="", flush=True)

    with terminal.location(y=terminal.height // 2):
        print(terminal.center(terminal.bold("Press any key to exit...")))

    terminal.inkey()
