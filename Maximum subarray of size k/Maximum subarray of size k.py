def max_sum_subarray(arr, k):
    n = len(arr) #Calculing len of arr
    if n < k:
        return "Array size is smaller than k"
    # Calculating the sum of the first window of size k
    window_sum = sum(arr[:k]) 
    max_sum = window_sum #Equating max_sum and window_sum 
    # Slide the window over the array
    for i in range(k, n):
        # Add the next element and remove the first element of the previous window
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
try:  #Input from the user
    arr = list(map(int, input("Enter the elements: ").split()))
    k = int(input("Enter the size of the subarray (k): "))
    result = max_sum_subarray(arr, k)
    print("Maximum sum of subarray of size k:", result)
except ValueError:
    print("Please enter proper integers for the array and k.")
