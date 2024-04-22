from astropy import units as u

s = 100 * u.meter
t = 20 * u.second
m = 100 * u.kilogram
v = s / t
a = v / t
f = m * a

print("v =", v)
print("a =", a)
print("f =", f)
