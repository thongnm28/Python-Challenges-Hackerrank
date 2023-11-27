import numpy as np

size = [int(x) for x in input().split()]
x = np.empty(size)

if size[0] == size[1]:
    for i in range(0, size[0]):
        arr1 = np.array([int(x) for x in input().split()])
        x[i] = arr1

print(np.mean(x, axis=1))
print(np.var(x, axis=0))
print(round(np.std(x, axis=None), 11))