from astropy import units as u

f = 100 / u.second

print(f)
print(f.to(u.Hz))
