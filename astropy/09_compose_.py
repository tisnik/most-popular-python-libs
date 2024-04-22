from astropy import units as u

t = u.fortnight

for c in t.compose():
    print(c)
