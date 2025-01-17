def reverse_and_remove_duplicates(s):
    seen = set()  # To track unique characters
    result = []   # To store the reversed string without duplicates and spaces
    # Traverse the string from the end
    for char in reversed(s):
        if char != ' ' and char not in seen:  # Ignore spaces and duplicates
            result.append(char)
            seen.add(char)
    return ''.join(result)
# Get input from the user
s = input("Enter a string: ")
output = reverse_and_remove_duplicates(s)
print("Output:", output)
