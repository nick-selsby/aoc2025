import numpy as np

with open("input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

idx = lines.index("")
ranges = [[int(y) for y in x.split("-")] for x in lines[:idx]]
ranges = sorted(ranges, key=lambda x: x[0])
new_ranges = [ranges[0]]

for range in ranges:
    last_range = new_ranges[-1]
    if range[0] <= last_range[1]:
        last_range[1] = max(range[1], last_range[1])
    else:
        new_ranges.append(range)

new_ranges = np.array(new_ranges)
count = np.sum(new_ranges[:, 1] - new_ranges[:, 0] + 1)
print(f"COUNT: {count}")