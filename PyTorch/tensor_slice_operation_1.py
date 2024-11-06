import torch

# konstrukce tenzoru
v1 = torch.arange(10, 20)
print(v1)

# konstrukce rezu z tenzoru prvniho radu
v2 = v1[2:8]
print(v2)

# konstrukce rezu z tenzoru prvniho radu
v3 = v1[2:8:2]
print(v3)

# konstrukce rezu z tenzoru prvniho radu
v4 = v1[-8:-2]
print(v4)

# konstrukce rezu z tenzoru prvniho radu
v5 = v1[:-2]
print(v5)

# konstrukce rezu z tenzoru prvniho radu
v6 = v1[-3:]
print(v6)

# konstrukce rezu z tenzoru prvniho radu
v7 = v1[10:0]
print(v7)

# konstrukce rezu z tenzoru prvniho radu
v8 = v1[10:1:-1]
print(v8)

