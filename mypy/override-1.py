from typing import override


class Fruit:
    def eat(self):
        pass

class Apple(Fruit):
    @override
    def eat(self):
        pass
