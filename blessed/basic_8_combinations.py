import blessed

terminal = blessed.Terminal()

textColors = (
        terminal.black,
        terminal.red,
        terminal.green,
        terminal.yellow,
        terminal.blue,
        terminal.magenta,
        terminal.cyan,
        terminal.white,
)

backgroundColors = (
        terminal.on_black,
        terminal.on_red,
        terminal.on_green,
        terminal.on_yellow,
        terminal.on_blue,
        terminal.on_magenta,
        terminal.on_cyan,
        terminal.on_white,
)

for textColor in textColors:
    for backgroundColor in backgroundColors:
        print(f"{textColor}{backgroundColor}XXXXX{terminal.normal} ", end="")
    print()
