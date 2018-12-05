# Calculates the best time to break into the lab

# Step 1: transfer the data into a matrix showing when the guard is awake and when they are asleep

import numpy as np

filename = 'Dec4_input.txt'

# Loading in data
file = open(filename, 'r')
input = file.read().splitlines()
input = np.sort(input) # sorting in chronological order

asleep_log              = np.zeros([10000,100,60]) # initializing the array of [#guards, #shifts, #minutes]
guard_shift_number_log  = np.zeros([10000], dtype = 'int') # counts how many shifts each guard has had so far
guard_number = 0
asleep_amount = np.zeros([60], dtype = 'int')
# Parsing data 
for i in range(len(input)):

    _, month, rest    = input[i].split("-")
    day, time, text   = rest.split(maxsplit = 2)
    minute            = int(time[3:5])
    
    # If we came upon a new guard
    if 'Guard' in text:
        
        # Write the previous guard's sleep log to their file
        asleep_log[guard_number][guard_shift_number_log[guard_number]] = asleep_amount
        
        
        guard_shift_number_log[guard_number] += 1        
        
        
        # Get the new guard's information
        _, guard_number, _, _ = text.split()
        guard_number = int(guard_number[1:len(guard_number)]) # now we know which guard we are dealing with
        asleep_amount = np.zeros([60])
    
    # If the guard just fell asleep
    if 'falls' in text:
        
        asleep_amount[minute:60] = np.ones([60 - minute], dtype = 'int')
        # Need to know which number of shift it is for this guard
        
    # If the guard just woke up
    if 'wakes' in text:
        asleep_amount[minute:60] = np.zeros([60 - minute], dtype = 'int')

# Done writing the data to aslee_log for each guard for each shift, now write the final entry
asleep_log[guard_number][guard_shift_number_log[guard_number]] = asleep_amount
guard_shift_number_log[guard_number] += 1     

# Ready to process the data!

# To find which guard sleeps the most, sum all of their shifts together
guard_sleep_count_minute_by_minute = np.sum(asleep_log, axis = 1) # gives a length [10000,60] array of how many times the each guard was asleep for each numbered minute
total_sleep_minutes_per_guard = np.sum(guard_sleep_count_minute_by_minute, axis = 1) # counts up how many minutes each guard was asleep

sleepiest_guard_number = np.argmax(total_sleep_minutes_per_guard) # guard number who was the sleepiest
sleepiest_guard_amount = total_sleep_minutes_per_guard[sleepiest_guard_number] # how long they've slept

# Finally, figure out which minute are they at their sleepiest
sleepiest_minute = np.argmax(guard_sleep_count_minute_by_minute[sleepiest_guard_number])

# Return output
print("Q1: The guard ID (%i) multiplied by their sleepiest minute (%i) is %i" %(sleepiest_guard_number, sleepiest_minute, (sleepiest_guard_number*sleepiest_minute)))


#%% Of all the guards, which guard is most frequently asleep on the same minute?
# Need to find how many times each guard has been asleep on a given minute.

each_guards_sleepiest_minute = np.argmax(guard_sleep_count_minute_by_minute, axis = 1)
each_guards_times_asleep_on_that_minute = np.max(guard_sleep_count_minute_by_minute, axis = 1)

sleepiest_guard_ID_on_a_minute = np.argmax(each_guards_times_asleep_on_that_minute)
sleepiest_minute_number = each_guards_sleepiest_minute[sleepiest_guard_ID_on_a_minute]

print("Q2: The guard ID (%i) multiplied by the minute they slept the most (%i) is %i" %(sleepiest_guard_ID_on_a_minute, sleepiest_minute_number, sleepiest_guard_ID_on_a_minute*sleepiest_minute_number))
