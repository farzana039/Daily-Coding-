def is_divisible_by_3(arr):
    digit_sum = 0
    # Iterate through each number in the array
    for num in arr:
        while num > 0:
            digit_sum += num % 10  # Add the last digit
            num //= 10  # Remove the last digit
    # Check if the sum of digits is divisible by 3
    if digit_sum % 3 == 0:
        return 1
    else:
        return 0
arr = list(map(int, input("Enter the array of integers separated by space: ").split()))
result = is_divisible_by_3(arr)
print(result)
