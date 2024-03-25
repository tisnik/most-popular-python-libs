l = []

for i in range(1001):
    m = []
    for j in range(1001):
        m.append(j)
    l.extend(m)

s = sum(l)
print(s)
