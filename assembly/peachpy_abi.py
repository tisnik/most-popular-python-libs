# Základy použití knihovny PeachPy
#
# - výpis ABI na aktuálně používaném počítači


# základní konstruktory atd.
from peachpy.x86_64 import abi

print(abi.detect())
