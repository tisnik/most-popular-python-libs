from rich.tree import Tree
from rich import print


tree = Tree("Barvové modely")
tree.add("RGB")
tree.add("CMYK")
tree.add("YUV")
tree.add("HSL")
tree.add("HSV")

print(tree)
