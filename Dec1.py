#%% Part 1

filename = 'Dec1_1_input.txt'

file = open(filename, 'r')

input = file.read().splitlines()

frequency = 0 # running total
for i in range(len(input)):
    frequency += int(input[i]) # find the new frequency
    
print("Q1: The ending frequency is %i" % frequency)


#%% Part 2

# Same input, which frequency is reached twice first?

frequency = 0 # running total
frequency_log = [] # Logging all frequencies reached
done = False
while not done:
        
    for i in range(len(input)):
        frequency += int(input[i]) # find the new frequency
    
        if frequency in frequency_log:
            print("Q2: Frequency %i has been reached twice!" % frequency)
            done = True
            break
        
        frequency_log.append(frequency) # logging all frequencies reached