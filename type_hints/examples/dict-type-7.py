# Typové anotace a nástroj Mypy:
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - hodnoty mohou nabývat None

from typing import Dict, Optional

d: Dict[str, Optional[float]] = {}

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = None

print(d)
