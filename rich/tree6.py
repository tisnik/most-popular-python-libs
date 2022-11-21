from rich.tree import Tree
from rich import print


tree = Tree("Barvové modely")
rgb = tree.add("RGB")
cmyk = tree.add("CMYK", expanded=False)
yuv = tree.add("YUV")
hsl = tree.add("HSL")
hsv = tree.add("HSV")

rgb.add("barva [red]Red")
rgb.add("barva [green]Green")
rgb.add("barva [blue]Blue")

cmyk.add("barva [cyan]Cyan")
cmyk.add("barva [magenta]Magenta")
cmyk.add("barva [yellow]Yellow")
cmyk.add("barva [black]blacK")

hsl.add("Hue")
hsl.add("Saturation")
hsl.add("Lightness")

hsv.add("Hue")
hsv.add("Saturation")
hsv.add("Value")

print(tree)
