from DSASorts import *
import numpy as np
print("TESTING EDGE SORT")
print()

b = [[10, 'e'], [10, 'f'], [10, 'g'], [7, 'd'], [2, 'a'], [4, 'b'], [5, 'c'], [202, 'f']]
a = np.empty(len(b), dtype=object)
for i,z in enumerate(b):
    temp = np.empty(2, dtype=object)
    temp[0] = z[0]
    temp[1] = z[1]
    a[i] = temp


print(a)
print()
print(DSASorts().edgeSort(a))
print()
print()
print(b)
print()
print(DSASorts().edgeSort(b))