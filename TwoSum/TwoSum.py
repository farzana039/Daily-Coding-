def twoSum(nums, target):
    index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index:
            return [index[complement], i]
        index[num] = i
nums = list(map(int, input("Enter the list of numbers: ").split()))
target = int(input("Enter the target value: "))
result = twoSum(nums, target)
print(f"The indices are: {result}")
