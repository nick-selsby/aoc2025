import numpy as np

with open("input.txt", "rb") as f:
    lines = [x.strip() for x in f.readlines()]

beams = np.frombuffer(lines[0], dtype=np.uint8) == ord('S')
splitters = np.array([np.frombuffer(line, dtype=np.uint8) == ord('^') for line in lines[1:]])
count = 0
for row in splitters:
    hits = beams & row
    count += np.sum(hits)
    beams = np.roll(hits, -1) | np.roll(hits, 1) | (beams & np.logical_not(row))

print(f"COUNT: {count}")