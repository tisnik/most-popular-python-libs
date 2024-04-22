from astropy import units as u

t = u.second

for c in t.compose():
    print(c)
