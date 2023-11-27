import numpy as np

n, _ = map(int, input().split())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

result = np.prod(np.sum(a, axis=0), axis=0)
print(result)