import ast


class Visitor(ast.NodeVisitor):
    def visit(self, node):
        print(node)
        self.generic_visit(node)


tree = ast.parse("1+2*3")

visitor = Visitor()
visitor.visit(tree)
