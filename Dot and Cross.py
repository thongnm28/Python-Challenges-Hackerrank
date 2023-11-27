import numpy as np

n = int(input())

A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

matrix_product = np.dot(A, B)

print(matrix_product)