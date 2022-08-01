import ast

tree = ast.parse("1+2*3")

for node in ast.walk(tree):
    print(node)
