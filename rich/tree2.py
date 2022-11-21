from rich.tree import Tree
from rich import print


tree = Tree("Barvové modely")
tree.add("RGB").add("Red Green Blue")
tree.add("CMYK").add("Cyan Magenta Yellow blacK")
tree.add("YUV").add("Luminance Chrominance")
tree.add("HSL").add("Hue Saturation Lightness")
tree.add("HSV").add("Hue Saturation Value")

print(tree)
