import numpy as np

n = int(input())
matrix = []
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

determinant = np.linalg.det(matrix)
rounded_determinant = round(determinant, 2)
print(rounded_determinant)