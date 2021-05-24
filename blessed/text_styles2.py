import blessed

terminal = blessed.Terminal()

print(f"{terminal.normal}normal text{terminal.normal}")
print(f"{terminal.bold}bold text{terminal.normal}")
print(f"{terminal.underline}underlined text{terminal.normal}")
print(f"{terminal.reverse}reversed text{terminal.normal}")
print()

print(f"{terminal.bold}bold{terminal.underline} and underlined{terminal.normal} text")
print()

print(f"{terminal.underline}underlined {terminal.reverse}and reversed{terminal.normal} text")
print()

print(f"{terminal.reverse}reversed {terminal.bold}and bold{terminal.normal} text")
