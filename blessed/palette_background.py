import blessed

terminal = blessed.Terminal()

terminal.number_of_colors = 1 << 24

for red in range(0, 256, 16):
    for green in range(0, 256, 16):
        for blue in range(0, 256, 16):
            hex_triplet = "#{:02x}{:02x}{:02x}".format(red, green, blue)
            print(terminal.on_color_rgb(red, green, blue) + hex_triplet, end=" ")
        print()
    print()

print()
print(f"{terminal.normal}DONE")
