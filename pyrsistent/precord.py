from pyrsistent import PRecord, field


class XYRecord(PRecord):
    x = field()
    y = field()


record1 = XYRecord(x=1)
print(record1)

record2 = record1.set("y", 42)
print(record2)

record3 = record2.set("z", 0)
print(record3)
