def distribute_tasks(arr, k):
    #  Find all remaining tasks
    all_tasks = set(range(1, k + 1)) # all tasks are in a set
    completed_tasks = set(arr) # completed tasks are in this set
    remaining_tasks = sorted(all_tasks - completed_tasks) # remaining tasks are calculated by substracting all taks and completed tasks
    #Distribute tasks alternately between Tanya and Manya
    tanya_tasks = []
    manya_tasks = []
    for i, task in enumerate(remaining_tasks): #enumerate allows you to iterate over a sequence 
        if i % 2 == 0:
            tanya_tasks.append(task)  # Tanya takes the 1st, 3rd, 5th...
        else:
            manya_tasks.append(task)  # Manya takes the 2nd, 4th, 6th...
    return [tanya_tasks, manya_tasks]
arr = [2, 5, 6, 7, 9, 4]
k = 15
result = distribute_tasks(arr, k)
print("Tanya's Tasks:", result[0])
print("Manya's Tasks:", result[1])
