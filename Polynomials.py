import numpy as np

lst = list(map(float, input().split()))
b = float(input())

result = np.polyval(lst, b)
print(result)