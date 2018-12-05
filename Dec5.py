# Determine the number of units left after the polymer reaction.

import numpy as np

filename = 'Dec5_input.txt'

# Loading in data
file = open(filename, 'r')
input = file.read()

#input = 'dabAcCaCBAcCcaDA'
input2 = input # for part 2

# Changing to a list so I can remove elements as I please
input = list(input)

def react(input):        
    
    done = False
    i = 0
    something_changed = False
    
    # from the first element to the second-last
    while not done:
        
        # If we are lower case and the next unit is uppercase of the same letter (or vice versa)
        try: # this will fail when we run past the end of the string -> will bring us to except
            if (input[i].islower() and (input[i].upper() == input[i+1])) or (input[i].isupper() and (input[i].lower() == input[i+1])):
            
                # These two units react and destroy each-other
                del input[i]
                del input[i] 
                something_changed = True
            else: # no reaction here, try the next element
                i += 1
        except: # we're done one iteration
            
            # if nothing changed, we're done!
            if not something_changed:
                break
            
            # Otherwise, reset and try again!
            i = 0
            something_changed = False
    
    return len(input)
    

final_length = react(input)
print("Q1: All done, the length of the reacted polymer is %i" % final_length)

#%% Remove one type completely (A/a, B/b, etc.) and react the remaining portion.
# What's the shortest length polymer that remains?

units_to_remove = np.unique(list(input2.upper())) # all the options we should try to remove
input2 = list(input2) # convert to list
final_length = []

for j in range(len(units_to_remove)):
    input_j = input2.copy() # reset the input. Note: you must copy the list to input_j or else input2 will be modified too!
    indices_to_remove = []
    
    indices_to_remove = [i for i, x in enumerate(input_j) if ((x == units_to_remove[j]) or (x == units_to_remove[j].lower()))]
    
    for k in range(len(indices_to_remove)):
        del input_j[indices_to_remove[k]-k] # cutting out those letters
    
    final_length.append(react(input_j))
    
    
print("Q2: The shortest polymer, of length %i, is achieved by removing unit %s" % (np.min(final_length), units_to_remove[np.argmin(final_length)]))
    