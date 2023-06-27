from typing import Dict, Union

d:Dict[str, Union[int, float, str]] = {}

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = "*"
d[10] = 10
d[42] = "answer"

reveal_type(d)
