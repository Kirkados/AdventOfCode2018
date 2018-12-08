# Find the order we should do all the steps

import string

filename = 'Dec7_input.txt'

# Loading in data
file = open(filename, 'r')
input = file.read().splitlines()

prerequisite_tree = {}
# Parsing input and placing it into a dict
for i in range(len(input)):
    _, pre_req, _, _, _, _, _, step, _, _ = input[i].split()
    
    # Try to append to this entry
    try:
        prerequisite_tree[step].append(pre_req)
    except: # If this entry doesn't exist yet, create it
        prerequisite_tree[step] = [pre_req]
    
prerequisite_tree_2 = prerequisite_tree.copy()
# create list to hold complete steps
dones = []
alphabet = string.ascii_uppercase

while len(prerequisite_tree) > 0:
    
    # From A to Z
    for i in range(len(alphabet)):
        
        # Try will fail if the alphabet letter doesn't exist in the dict
        try:
            
            # if all prerequisites are satisfied for that element
            if all([pre_req in dones for pre_req in prerequisite_tree[alphabet[i]]]):
                
                # This step has been done, remove it from the pre-req tree
                del prerequisite_tree[alphabet[i]]
                
                # Append it to the done list
                dones.append(alphabet[i])
                
                # Start loop over from the beginning
                break
        except:
            if not alphabet[i] in dones:
                dones.append(alphabet[i])
                break
# All done!
print("Q1: The order is %s" % ''.join(dones))

#%% If you have N workers, and it takes 60 + letter_number to complete each step,
#   how long does it take to finish all steps? The order will change

# Each letter is put on held for that number of seconds (1 loop = 1 second)
dones = [] # which letters are done
seconds = 0
N_workers = 5
worker_tasks = {} # which workers are currently working on which letters and how much longer do they have
free_workers = list(range(N_workers)) # number of idle workers

while (len(prerequisite_tree_2) > 0) or (len(worker_tasks) > 0): # while there are letters left or workers are still working
    # From A to Z
    for i in range(len(alphabet)):        
        # Try will fail if the alphabet letter doesn't exist in the prerequisite_tree_2
        try:            
            # if all prerequisites are satisfied for that element
            if all([pre_req in dones for pre_req in prerequisite_tree_2[alphabet[i]]]):
                # Give it to the first worker on the list of free workers
                try:
                    worker_tasks[free_workers[0]] = [alphabet[i], ord(alphabet[i]) - 4] # worker_tasks[worker number] = ['A', 61]
                    del free_workers[0] # worker now busy
                    del prerequisite_tree_2[alphabet[i]] # this step is no longer in the tree as it's being worked on
                except:
                    # If there are no workers available, continue to the next loop
                    pass                
        except: # fails when alphabet[i] is not in the prerequisite_tree_2 (i.e., the initial letters)
            worker_keys = list(worker_tasks.keys())
            
            # if this letter isn't already done, AND if it's not already being worked on, try to start it up
            if (not (alphabet[i] in dones)) and (not (any([alphabet[i] in worker_tasks[worker_keys[k]][0] for k in range(len(worker_tasks))]))): 
                try:
                    worker_tasks[free_workers[0]] = [alphabet[i], ord(alphabet[i]) - 4] # worker_tasks[worker number] = ['A', 61]
                    del free_workers[0] # that worker is now working!
                except:
                    # If there are no workers available, break to the next loop
                    pass        
        continue        
    
    worker_keys = list(worker_tasks.keys()) # generate all the keys for the worker_tasks dictionary
    # print(seconds, worker_tasks, free_workers)
    # All workers can decrease their tasks by 1 second... possibly workers will free up here and tasks will be done
    for j in range(len(worker_tasks)): # For each worker who is currently working
        worker_tasks[worker_keys[j]][1] -= 1 # reduce the time left by one second

        # Check if the task is done!
        if worker_tasks[worker_keys[j]][1] == 0:
            # This worker is done their task!
            dones.append(worker_tasks[worker_keys[j]][0]) # add the letter to the dones list
            free_workers.append(worker_keys[j]) # add this worker to the 'free workers' list            
            del worker_tasks[worker_keys[j]] # remove this task from the in-progress task list    
    
    seconds += 1
    
# All done!
print("Q2: The order is %s, and it took %i seconds" % (''.join(dones), seconds))