import blessed

terminal = blessed.Terminal()

print(f"{terminal.on_black}black background{terminal.normal}")
print(f"{terminal.on_red}red background{terminal.normal}")
print(f"{terminal.on_green}green background{terminal.normal}")
print(f"{terminal.on_yellow}yellow background{terminal.normal}")
print(f"{terminal.on_blue}blue background{terminal.normal}")
print(f"{terminal.on_magenta}magenta background{terminal.normal}")
print(f"{terminal.on_cyan}cyan background{terminal.normal}")
print(f"{terminal.on_white}white background{terminal.normal}")
