import torch

# konstrukce tenzoru
m1 = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("m1:")
print(m1)
print("Stride:", m1.stride())
print("Offset:", m1.storage_offset())
print("Contiguous:", m1.is_contiguous())
print()

m2 = m1[1:3]
print("m2:")
print(m2)
print("Stride:", m2.stride())
print("Offset:", m2.storage_offset())
print("Contiguous:", m2.is_contiguous())
print()

m3 = m1[:,1:3]
print("m3:")
print(m3)
print("Stride:", m3.stride())
print("Offset:", m3.storage_offset())
print("Contiguous:", m3.is_contiguous())
print()

m4 = m1[1:3,1:3]
print("m4:")
print(m4)
print("Stride:", m4.stride())
print("Offset:", m4.storage_offset())
print("Contiguous:", m4.is_contiguous())
print()
