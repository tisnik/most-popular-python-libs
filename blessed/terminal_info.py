import blessed

terminal = blessed.Terminal()

print("Resolution: {}x{} characters".format(terminal.width, terminal.height))
print("Number of colors: {}".format(terminal.number_of_colors))
