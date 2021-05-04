from PIL import Image
import blessed

terminal = blessed.Terminal()

terminal.number_of_colors = 1 << 24

filename = "fruits.png"
img = Image.open(filename)

for j in range(0, img.height, 2):
    for i in range(img.width):
        red, green, blue = img.getpixel((i, j))
        print(f"{terminal.on_color_rgb(red, green, blue)}.", end="")
    print()

print()
print(f"{terminal.normal}DONE")
