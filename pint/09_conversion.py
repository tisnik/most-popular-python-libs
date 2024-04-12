from pint import UnitRegistry

ureg = UnitRegistry()

s1 = 1000 * ureg.meter
s2 = s1.to(ureg.millimetre)
s3 = s1.to(ureg.nautical_mile)
s4 = s1.to(ureg.inch)

print(s1, s1.dimensionality)
print(s2, s2.dimensionality)
print(s3, s3.dimensionality)
print(s4, s4.dimensionality)
