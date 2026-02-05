import numpy as np
A = np.random.randint(0,100,(4,5))
print("Array used:\n", A, "\n")
print("Reversed Rows:\n", A[:,::-1], "\n")
print("Maximum of each row: ",A.max(axis=1), "\n")
print("Average of each column: ",A.mean(axis=0), "\n")
print("Reshaped Array:\n", A.reshape((5,4)))
