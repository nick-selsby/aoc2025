import numpy as np

tiles = np.genfromtxt("input.txt", dtype=np.int64, delimiter=",")
COUNT = tiles.shape[0]
INDICES = np.indices((COUNT, COUNT))
rect_sizes = np.prod(np.abs(tiles[INDICES[0]] - tiles[INDICES[1]]) + (1, 1), axis=2)

g_size = np.max(tiles) + 1
g_min_x = np.tile(10000000, g_size)
g_max_x = np.tile(-10000000, g_size)
g_min_y = np.tile(10000000, g_size)
g_max_y = np.tile(-10000000, g_size)
for i in range(len(tiles)):
    A = np.take(tiles, i, axis=0)
    B = np.take(tiles, i + 1, mode="wrap", axis=0)
    min_x, min_y = np.min((A, B), axis=0)
    max_x, max_y = np.max((A, B), axis=0)
    g_min_x[min_y:max_y+1] = np.minimum(g_min_x[min_y:max_y+1], min_x)
    g_max_x[min_y:max_y+1] = np.maximum(g_max_x[min_y:max_y+1], max_x)
    g_min_y[min_x:max_x+1] = np.minimum(g_min_y[min_x:max_x+1], min_y)
    g_max_y[min_x:max_x+1] = np.maximum(g_max_y[min_x:max_x+1], max_y)

valid_rects = np.full(rect_sizes.shape, False)

for x in range(COUNT):
    for y in range(COUNT):
        A = np.take(tiles, x, axis=0)
        B = np.take(tiles, y, axis=0)
        min_x, min_y = np.min((A, B), axis=0)
        max_x, max_y = np.max((A, B), axis=0)
        C1 = np.all(g_min_x[min_y:max_y+1] <= min_x)
        C2 = np.all(g_max_x[min_y:max_y+1] >= max_x)
        C3 = np.all(g_min_y[min_x:max_x+1] <= min_y)
        C4 = np.all(g_max_y[min_x:max_x+1] >= max_y)
        valid_rects[x, y] = C1&C2&C3&C4

rect_sizes = rect_sizes * valid_rects 
print(f"LARGEST RECT TILE INDEXES\t{np.unravel_index(np.argmax(rect_sizes), valid_rects.shape)}")
print(f"OUTPUT\t\t\t\t{np.max(rect_sizes)}")