def missing(arr,N):
 total_sum=N*(N+1)/2 #total sum till N numbers
 arr_sum=sum(arr) # sum of elements in arr
 missing=(total_sum)-(arr_sum) # missing number can be calculated using totalsum-sum
 return missing
# Taking input from the user
N = int(input("Enter the value of N: "))
print(f"Enter {N-1} distinct integers in the range 1 to {N}:")
arr = list(map(int, input().split()))
# Ensure the input size matches the expected size
if len(arr) != N - 1:
    print(f"Enter exactly {N-1} integers!")
else:
    # Find and print the missing element
    missing = missing(arr, N)
    print("Missing element:", missing)
