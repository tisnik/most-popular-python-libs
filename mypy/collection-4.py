class Collection[T]():
    def __init__(self) -> None:
        self.collection : list[T] = []

    def append(self, item: T) -> None:
        self.collection.append(item)

    def get_all(self) -> list[T]:
        return self.collection


c = Collection[int]()
c.append(1)
c.append("foo")
