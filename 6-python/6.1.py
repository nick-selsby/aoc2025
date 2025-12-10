import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

nums = np.array([[int(i) for i in x.strip().split()] for x in lines[:-1]])
sym = np.array([i == '*' for i in lines[-1].strip().split()])
values = np.where(sym, np.prod(nums, axis=0), np.sum(nums, axis=0))
final = np.sum(values)

print(f"OUTPUT: {final}")