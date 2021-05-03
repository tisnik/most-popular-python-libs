import blessed

terminal = blessed.Terminal()

print(terminal.normal + "normal text")
print(terminal.bold + "bold text" + terminal.normal)
print(terminal.underline + "underlined text" + terminal.normal)
print(terminal.reverse + "reversed text" + terminal.normal)
print()

print(terminal.bold + "bold " + terminal.underline + "and underlined " + terminal.normal + "text")
print()

print(terminal.underline + "underlined " + terminal.reverse + "and reversed " + terminal.normal + "text")
print()

print(terminal.reverse + "reversed " + terminal.bold + "and bold " + terminal.normal + "text")
