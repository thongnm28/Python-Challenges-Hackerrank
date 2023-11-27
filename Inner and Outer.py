import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

inner_product = np.inner(A, B)
outer_product = np.outer(A, B)

print(inner_product)
print(outer_product)