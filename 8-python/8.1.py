import numpy as np

input = np.genfromtxt("input.txt", dtype=np.float32, delimiter=",") #read from file
COUNT = input.shape[0]
#create a NxN table where the distance from each box to each other box is stored
indices = np.indices((COUNT, COUNT))
box_distances = np.sum(np.square(input[indices[0,:,:]] - input[indices[1,:,:]]), axis=2)
#prevent boxes linking to themselves
box_distances[box_distances == 0.0] = np.inf
#assign a circuit number to each box that can be merged later
circuits = np.arange(COUNT)

for iteration in range(1000):
    # get the shortest distance idx
    flat_idx = np.argmin(box_distances) #get smallest distance
    idx = np.unravel_index(flat_idx, box_distances.shape)
    # mark these boxes so they can't be chosen again
    box_distances[idx] = np.inf
    box_distances[idx[::-1]] = np.inf
    # every box that belonged to circuit A now belongs to circuit B, increasing the circuit's size
    old_circuit = circuits[idx[1]]
    new_circuit = circuits[idx[0]]
    circuits[circuits == old_circuit] = new_circuit

# count the circuits, choose the largest 3 and multiply their sizes as specified by AoC
remaining_circuits, circuit_counts = np.unique(circuits, return_counts=True)
output = np.prod(np.sort(circuit_counts)[-3:])

print(f"OUTPUT: {output}")