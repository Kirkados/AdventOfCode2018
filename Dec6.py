# For a given list of coordinates, find the L1 norm for all the points.
# A point with the smallest L1 norm for a coordinate is deemed to belong to that coordinate
# Which coordinate has the most points associated with it, and that isn't infinite?

import numpy as np

filename = 'Dec6_input.txt'

# Loading in data
file = open(filename, 'r')
input = file.read().splitlines()

data = np.zeros([len(input), 2]) # [num entries, xy column]

grid_size = 500

# Parse into array
for i in range(len(input)):
    first, second = input[i].split(',')
    data[i] = [int(first), int(second)]

grid = []
for i in range(-grid_size, grid_size + 1):

    grid.append([[i, y] for y in range(-grid_size, grid_size + 1)])
        
# Now we have a grid of data points. For example, grid[x][y] gives an array with the (x,y) position

# Let's tile that for all entries
tiled_grid = []
tiled_grid.append([grid.copy() for i in range(len(data))]) # dimensions =[1, entry, x, y]

# Calculating manhatten distances
for i in range(len(data)):
    tiled_grid[0][i] = np.abs(tiled_grid[0][i][:][:] - data[i])

# Tiled grid is the L1 norms now
L1_norms = np.sum(tiled_grid, axis = 0) # getting rid of 1st dimension
L1_norms = np.abs(np.sum(L1_norms, axis = 3)) # calculating L1 norm

# Now we know the L1 norms for each entry, for each point. 
# Now, for all points, find which entry has the lowest L1 norm (excluding ties)

#mins = np.argmin(L1_norms, axis = 0) # argmin gives the minimums, but it does not account for duplicates.
all_minimum_indices = np.where(L1_norms == L1_norms.min(axis = 0))

entry_counter = np.zeros([len(input)])
# I'll send all the duplicate minimum indices to huge numbers 
for i in range(len(all_minimum_indices[0])):
    
    # ERROR BELOW -> NEED TO make sure they index exists but also that it's in the same position as the other
    if not ([all_minimum_indices[1][i], all_minimum_indices[2][i]] in [[all_minimum_indices[1][j], all_minimum_indices[2][j]] for j in range(i+1, len(all_minimum_indices[0]))]):
        # this entry is the minimum list only once, add it to the appropriate entry's counter (ignore duplicates)
        entry_counter[all_minimum_indices[0][i]] += 1

print(entry_counter)