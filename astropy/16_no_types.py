from astropy import units as u


def velocity(s, t):
    return s/t

s = 100 * u.meter
t = 20 * u.second
v = velocity(s, t)

print(v)
