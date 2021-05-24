"""Zjištění základních informací o správci paměti."""

import gc

print(gc.get_threshold())
print(gc.get_count())

gc.collect()
print(gc.get_count())
