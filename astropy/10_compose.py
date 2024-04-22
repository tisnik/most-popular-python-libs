from astropy import units as u

t = u.second ** -1

for c in t.compose():
    print(c)
