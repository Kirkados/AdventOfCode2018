# Compute the checksum by counting letters

# If a word has exactly two of a letter, that word is added to the "twos" counter
# If a word has exactly three of a letter, that word is added to the "threes" counter

# The final checksum is the product of both counters.

import numpy as np

filename = 'Dec2_input.txt'

# Loading in data
file = open(filename, 'r')
input = file.read().splitlines()

# Initializing counters
twos_counter   = 0
threes_counter = 0

# For each entry
for i in range(len(input)):
    
    # Split each entry into its characters
    character_array = list(input[i])
    
    # Find number of unique characters in that string
    _, counts = np.unique(ar = character_array, return_counts = True)
    
    # Is some letter in there twice?
    if np.any(2 == counts):
        twos_counter += 1
    
    # Is some letter in there thrice?
    if np.any(3 == counts):
        threes_counter += 1
        
print("The checksum is %i" % (twos_counter*threes_counter))

#%% Part 2 - Find which entries differ by only one letter

# Couldn't come up with a more elegant way, so I'll just loop through brute-force style

done = False

# For each entry
for i in range(len(input)):
    
    # Comparing it with each remaining entry excluding itself
    for j in range(i+1, len(input)):
        
        not_same_counter = 0 # counts how many letters are not the same between the two entries
        
        # For each letter in the entry
        for k in range(len(input[i])):            
            
            # If the letters at this location are not the same
            if input[i][k] != input[j][k]:
                not_same_counter += 1
                element_to_remove = k
                
                # If these two entries are too dissimilar
                if not_same_counter == 2:
                    break
            
        if not_same_counter == 1:
            # We found the fabric!!
            print("The fabric is in entry %s and %s with the difference being with element %i" %(input[i], input[j], element_to_remove) )
            done = True
            break
    
    if done:
        break

# Answer pbykrmjmizwhxlqnasfgtycdv