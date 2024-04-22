from astropy import units as u

l = 100 * u.meter

print(l)
print(l.to(u.Hz, equivalencies=u.spectral()))
