import blessed

terminal = blessed.Terminal()

print(f"{terminal.bold_black}black text{terminal.normal}")
print(f"{terminal.bold_red}red text{terminal.normal}")
print(f"{terminal.bold_green}green text{terminal.normal}")
print(f"{terminal.bold_yellow}yellow text{terminal.normal}")
print(f"{terminal.bold_blue}blue text{terminal.normal}")
print(f"{terminal.bold_magenta}magenta text{terminal.normal}")
print(f"{terminal.bold_cyan}cyan text{terminal.normal}")
print(f"{terminal.bold_white}white text{terminal.normal}")
