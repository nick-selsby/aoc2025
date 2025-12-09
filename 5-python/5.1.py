import numpy as np

with open("input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

idx = lines.index("")
ranges = np.array([[int(y) for y in x.split("-")] for x in lines[:idx]])
ids = [int(x) for x in lines[idx+1:]]

count = 0
for id in ids:
    if np.any((id >= ranges[:, 0]) & (id <= ranges[:, 1])):
        count += 1

print(f"COUNT: {count}")