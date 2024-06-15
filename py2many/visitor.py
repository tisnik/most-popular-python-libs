class Visitor():
    def __init__(self):
        self.nest_level = 0

    def on_visit(self, text):
        indent = " " * self.nest_level * 2
        print(indent, text)
        self.nest_level += 1

    def on_leave(self, node):
        self.nest_level -= 1
