def is_isogram(s):
    s = s.lower()  # Step 1: Convert the input string to lowercase to ensure case insensitivity
    seen = set()   # Step 2: Create an empty set to track characters we've already encountered
    for char in s:  # Step 3: Iterate through each character in the string
        if char.isalpha():  # Step 4: Check if the character is an alphabet (ignore spaces, numbers, and symbols)
            if char in seen:  # Step 5: If the character is already in the set, it's a duplicate
                return False  # Return False because it's not an isogram
            seen.add(char)  # Step 6: Add the character to the set to track it as seen
    return True  # Step 7: If no duplicates are found, return True (it's an isogram)
word = input("Enter a word or phrase: ")
if is_isogram(word):
    print(f"'{word}' is an isogram.")
else:
    print(f"'{word}' is not an isogram.")
