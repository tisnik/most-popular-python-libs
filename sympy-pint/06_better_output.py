from pint import UnitRegistry
import sympy as sp

ureg = UnitRegistry()

m = sp.Symbol("m") * ureg.kilogram
t = sp.Symbol("t") * ureg.second
s = sp.Symbol("s") * ureg.meter
v = s/t
a = v/t
f = m*a

print(f"{m.magnitude} \t [{m.units}]")
print(f"{t.magnitude} \t [{t.units}]")
print(f"{v.magnitude} \t [{v.units}]")
print(f"{a.magnitude} \t [{a.units}]")
print(f"{f.magnitude} \t [{f.units}]")
