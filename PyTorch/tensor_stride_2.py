import torch

# konstrukce tenzoru
v1 = torch.arange(10, 20)
print("v1:")
print(v1)
print("Stride:", v1.stride())
print("Offset:", v1.storage_offset())
print()

# konstrukce tenzoru - rezu
v2 = v1[:5]
print("v2:")
print(v2)
print("Stride:", v2.stride())
print("Offset:", v2.storage_offset())
print()

# konstrukce tenzoru - rezu
v3 = v1[5:10]
print("v3:")
print(v3)
print("Stride:", v3.stride())
print("Offset:", v3.storage_offset())
print()

# konstrukce tenzoru - rezu
v4 = v1[::3]
print("v4:")
print(v4)
print("Stride:", v4.stride())
print("Offset:", v4.storage_offset())
print()

# konstrukce tenzoru - rezu
v5 = v1[2::3]
print("v5:")
print(v5)
print("Stride:", v5.stride())
print("Offset:", v5.storage_offset())
print()

