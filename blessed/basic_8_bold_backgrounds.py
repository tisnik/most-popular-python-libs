import blessed

terminal = blessed.Terminal()

print(f"{terminal.bold_on_black}black background{terminal.normal}")
print(f"{terminal.bold_on_red}red background{terminal.normal}")
print(f"{terminal.bold_on_green}green background{terminal.normal}")
print(f"{terminal.bold_on_yellow}yellow background{terminal.normal}")
print(f"{terminal.bold_on_blue}blue background{terminal.normal}")
print(f"{terminal.bold_on_magenta}magenta background{terminal.normal}")
print(f"{terminal.bold_on_cyan}cyan background{terminal.normal}")
print(f"{terminal.bold_on_white}white background{terminal.normal}")
