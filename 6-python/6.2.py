import numpy as np

with open("input.txt", "rb") as f:
    lines = f.readlines()

nums = np.array([np.frombuffer(x.strip(), dtype=np.uint8) for x in lines[:-1]])
nums = np.pad(nums, ((0, 0), (1, 1)), "constant", constant_values=32)
sym = np.array([i == b'*' for i in lines[-1].strip().split()])
spaces = np.all(nums == 32, axis=0)
columns = np.arange(nums.shape[1])[spaces]
final = 0
for i in range(len(columns) - 1):
    val_array = []
    for a_idx, j in enumerate(range(columns[i] + 1, columns[i + 1])):
        v = int("".join([chr(nums[row][j]) for row in range(nums.shape[0])]))
        val_array.append(v)
    
    if sym[i]:
        problem_total = np.prod(val_array)
    else:
        problem_total = np.sum(val_array)
    
    final += problem_total

print(f"COUNT: {final}")