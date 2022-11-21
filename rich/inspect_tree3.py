from rich import inspect
from rich.tree import Tree

tree = Tree("Strom")
node = tree.add("Uzel")

inspect(node)
