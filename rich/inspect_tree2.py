from rich import inspect
from rich.tree import Tree

tree = Tree("Barvové modely")
tree.add("RGB")
tree.add("CMYK")
tree.add("YUV")
tree.add("HSL")
tree.add("HSV")

inspect(tree, methods=True)
