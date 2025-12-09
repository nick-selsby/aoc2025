import numpy as np
from scipy.ndimage import convolve

with open("input.txt", "rb") as f:
    arr = np.array([np.frombuffer(line.strip(), dtype=np.uint8) for line in f.readlines()])

arr = (arr == 64).astype(np.uint8)
arr = np.pad(arr, ((1, 1), (1, 1)), "constant", constant_values=0)
total = 0
while True:
    convolved = convolve(arr, [[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    t = (convolved < 4) & (arr > 0)
    current_sum = np.sum(t)
    if current_sum == 0: break
    arr[t] = 0
    total += current_sum

print(f"PAPERS AVAILABLE: {total}")