import numpy as np

with open("input.txt", "rb") as f:
    lines = [x.strip() for x in f.readlines()]

beams = (np.frombuffer(lines[0], dtype=np.uint8) == ord('S')).astype(np.uint64)
splitters = np.array([np.frombuffer(line, dtype=np.uint8) == ord('^') for line in lines[1:]])
for row in splitters:
    hits = beams * row
    beams = np.roll(hits, -1) + np.roll(hits, 1) + (beams * np.logical_not(row))

count = np.sum(beams)
print(f"COUNT: {count}")