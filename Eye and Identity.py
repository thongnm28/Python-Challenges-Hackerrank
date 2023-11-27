import numpy as np

np.set_printoptions(legacy="1.13")

R, C = map(int, input().split())

identidad = np.eye(R, C, k=0)
print(identidad)