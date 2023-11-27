import numpy as np

if __name__ == "__main__":
    m, n = map(int, input().split())
    arr = np.array([input().split() for _ in range(m)], int)
    print(np.max(np.min(arr, axis=1)))