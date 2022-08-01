import ast
  
with open("async.py") as fin:
    code = fin.read()
    tree = ast.parse(code)

print(ast.dump(tree, indent=4))

