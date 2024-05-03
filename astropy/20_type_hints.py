from astropy import units as u


def velocity(s: u.Quantity[u.meter], t: u.Quantity[u.second]) -> u.Quantity[u.meter/u.second]:
    return s/t

s = 100 * u.meter
t = 20 * u.second
v = velocity(s, t)

print(v)
