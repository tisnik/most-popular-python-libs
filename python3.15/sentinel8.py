NA = sentinel("N/A")

values: dict[str, int | NA | None] = {}

values["foo"] = 42
values["bar"] = NA
values["baz"] = None

print(values)
