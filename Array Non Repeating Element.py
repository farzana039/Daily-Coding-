def array_non_repeating_element(arr):
    ans = 0
    for num in arr:
        ans ^= num  #this xor operation stores only non duplicate elements
    return ans
arr = list(map(int, input("Enter number ").split()))
print(array_non_repeating_element(arr)) 
  
