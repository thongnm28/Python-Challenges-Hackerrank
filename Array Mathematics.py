import numpy as np

n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]

a = np.array(a)
b = np.array(b)

print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))