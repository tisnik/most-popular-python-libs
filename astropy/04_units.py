from astropy import units as u

t1 = 10 * u.second
t2 = 1 * u.minute
t3 = 1 * u.second

print(t1.unit)
print(t2.unit)
print((t1*t1).unit)
print((1/t1).unit)
print((t1+t2).unit)
print((t1-t2).unit)
print((t2/t1).unit)
print((t1/t3).unit)
