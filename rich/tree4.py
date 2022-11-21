from rich.tree import Tree
from rich import print


tree = Tree("Barvové modely")
rgb = tree.add("RGB")
cmyk = tree.add("CMYK")
yuv = tree.add("YUV")
hsl = tree.add("HSL")
hsv = tree.add("HSV")

rgb.add("[red]Red")
rgb.add("[green]Green")
rgb.add("[blue]Blue")

cmyk.add("[cyan]Cyan")
cmyk.add("[magenta]Magenta")
cmyk.add("[yellow]Yellow")
cmyk.add("[black]blacK")

hsl.add("Hue")
hsl.add("Saturation")
hsl.add("Lightness")

hsv.add("Hue")
hsv.add("Saturation")
hsv.add("Value")

print(tree)
