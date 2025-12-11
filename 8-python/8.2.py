import numpy as np

positions = np.genfromtxt("input.txt", dtype=np.uint64, delimiter=",") #read from file
COUNT = positions.shape[0]
#create a NxN table where the distance from each box to each other box is stored
indices = np.indices((COUNT, COUNT))
box_distances = np.sum(np.square(positions[indices[0,:,:]] - positions[indices[1,:,:]]), axis=2)
#prevent boxes linking to themselves
HUGE = np.iinfo(box_distances.dtype).max
box_distances[box_distances == 0] = HUGE
#assign a circuit number to each box that can be merged later
circuits = np.arange(COUNT)

while True:
    # get the shortest distance idx
    flat_idx = np.argmin(box_distances) #get smallest distance
    idx = np.unravel_index(flat_idx, box_distances.shape)
    # mark these boxes so they can't be chosen again
    box_distances[idx] = HUGE
    box_distances[idx[::-1]] = HUGE
    # every box that belonged to circuit A now belongs to circuit B, increasing the circuit's size
    old_circuit = circuits[idx[1]]
    new_circuit = circuits[idx[0]]
    circuits[circuits == old_circuit] = new_circuit
    #if all circuits are the same, we have completed the task
    if np.all(circuits == circuits[0]): break

# we need to multiply the x coords of the last two boxes linked
output = np.prod(positions[idx, 0])
print(f"OUTPUT: {output}")