import numpy as np
L = np.random.randint(60,240,(10,12))
print(L)
print("dimensions=", L.ndim)
print("shape=", L.shape)
print("size=", L.size)
print("data type=", L.dtype)
print("item size=", L.itemsize)
print("total number of bytes=", L.nbytes)

print("Price of fruit B in the 4th Month is", L[1,3])

L1 = L[:, 0:3]
L2 = L[:, 3:6]
L3 = L[:, 6:9]
L4 = L[:, 9:]

print("First Quarter:\n", L1)
print("Second Quarter:\n", L2) 
print("Third Quarter:\n", L3)
print("Fourth Quarter:\n", L4)

