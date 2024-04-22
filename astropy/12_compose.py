from astropy import units as u

t = u.kilogram * u.meter / u.second ** 2

for c in t.compose():
    print(c)
