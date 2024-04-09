from typing_extensions import override


class Fruit:
    def eat(self) -> None:
        pass

class Apple(Fruit):
    @override
    def eat_apple(self) -> None:
        pass
