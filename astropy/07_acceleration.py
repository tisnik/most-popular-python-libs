from astropy import units as u

s = 100 * u.meter
t = 20 * u.second
v = s / t
a = v / t

print("v =", v)
print("a =", a)
