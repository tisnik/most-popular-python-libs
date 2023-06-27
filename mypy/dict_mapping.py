from typing import Dict, Mapping

d1:Dict[str, float] = {}

d1["foo"] = 1
d1["bar"] = 3.14
d1["baz"] = 0.0

print(d1)

d2:Mapping[str, float] = {}

d2["foo"] = 1
d2["bar"] = 3.14
d2["baz"] = 0.0

print(d2)
