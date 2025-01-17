def first_non_repeating_character(s):
    char_count = {}     #Count character frequencies and maintain order using a list
    char_order = []  # To maintain the order of characters
    for char in s:
        if char not in char_count:
            char_count[char] = 1
            char_order.append(char)  # Add to order list when first seen
        else:
            char_count[char] += 1
    # Step 2: Iterate list to find the first non-repeating character
    for char in char_order:
        if char_count[char] == 1:
            return char
    # Step 3: If no non-repeating character is found, return -1
    return -1
s = input("Enter a string: ")
result = first_non_repeating_character(s)
print(result)
