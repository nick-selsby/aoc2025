import numpy as np

tiles = np.genfromtxt("input.txt", dtype=np.int64, delimiter=",")
COUNT = tiles.shape[0]
INDICES = np.indices((COUNT, COUNT))
rect_sizes = np.prod(np.abs(tiles[INDICES[0]] - tiles[INDICES[1]]) + (1, 1), axis=2)
output = np.max(rect_sizes)
print(f"OUTPUT\t{output}")