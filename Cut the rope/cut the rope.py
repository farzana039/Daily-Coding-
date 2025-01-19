def count_ropes_after_cuts(arr):
    arr.sort() #Sort the array
    result = []
    prev_length = 0 #Perform cut operations
    n = len(arr)
    for i in range(n):
        if arr[i] > prev_length:
            result.append(n - i)  # Count ropes left after this cut
            prev_length = arr[i]  # Update previous cut length
    return result
arr1 = [5, 1, 1, 2, 3, 5]
arr2 = [5, 1, 6, 9, 8, 11, 2, 2, 6, 5]
print(count_ropes_after_cuts(arr1))  
print(count_ropes_after_cuts(arr2))  
