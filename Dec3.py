# The Elves all want a piece of the fabric for their own.
# How many square inches overlap?

import numpy as np
import time

filename = 'Dec3_input.txt'

# Loading in data
file = open(filename, 'r')
input = file.read().splitlines()

data = np.zeros([len(input), 5], dtype = "int") # [ID, X_edge, Y_edge, width_x, width_y]

# Parsing data 
for i in range(len(input)):
    _, rest          = input[i].split("#")
    ID, rest         = rest.split("@")
    X_edge, rest     = rest.split(",")
    Y_edge, rest     = rest.split(":")
    width_x, width_y = rest.split("x")
    
    data[i][0] = int(ID)
    data[i][1] = int(X_edge)
    data[i][2] = int(Y_edge)
    data[i][3] = int(width_x)
    data[i][4] = int(width_y)
    
# Write the location of each inch of fabric for each piece of fabric

locations = [] # for each location, this holds all the x entries and y entries (but not all the [x,y] combinations)

for i in range(len(input)):
    this_section_locations = [data[i][1] + [l for l in range(data[i][3])], data[i][2] + [l for l in range(data[i][4])]]
    locations.append(this_section_locations)
    
start_time = time.time()
overlapped_locations = []
overlap = 0
# Scan for overlaps    
for i in range(len(locations)):
    
    # For all other pieces of fabric
    for j in range(i, len(locations)):
        
        # Could check if these boxes are remotely overlapping, but I'll skip that and go more brute-force
        
        # For each column in original fabric
        for x in range(len(locations[i][0])):
            
            # For each row in original fabric
            for y in range(len(locations[i][1])):
                
                # For each column in the target piece of fabric
                for x_target in range(len(locations[j][0])):
                    
                    # For each row in the target piece of fabric
                    for y_target in range(len(locations[j][1])):
                        
                        # Does the (x,y) of the original equal the (x,y) of the target -> inicating overlap
                        if (locations[i][0][x] == locations[j][0][x_target]) and (locations[i][1][y] == locations[j][1][y_target]):
                            
                            count_it = True 
                            
                            # Before counting it, need to check if this location has been overlapped in the past (because overlap only counts once)
                            for m in range(len(overlapped_locations)):
                                
                                if [locations[i][0][x], locations[i][1][y]] == overlapped_locations[m]:
                                    
                                    # This point has already been counted
                                    count_it = False
                            
                            
                            if count_it:
                                overlap += 1
                                #print("overlapped")
                                overlapped_locations.append([locations[i][0][x], locations[i][1][y]])
    print("i = %i" %(i))

print("Done! It took %.1f s and we found %i overlapping square inches!" %(time.time() - start_time, overlap))