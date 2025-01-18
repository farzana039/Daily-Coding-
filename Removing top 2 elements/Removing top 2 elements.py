def remove_top_two_and_sort(arr):
    arr.sort()  # Sorting makes to remove top 2 elements easily
    if len(arr) >= 2:
     result = arr[:-2]  # Remove the last two elements
    else:
     result = []# If the array has fewer less than 2 elements simply return empty result
    return result   
try:
    user_input = input("Enter the elements of the array : ")
    arr = list(map(int, user_input.split()))
    result = remove_top_two_and_sort(arr)
    print("The sorted array after removing the top 2 maximum numbers:", result)
except ValueError:
    print("Invalid input! Please enter integers only.")
