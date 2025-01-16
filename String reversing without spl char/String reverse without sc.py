def reverse_string(S):
    # Extract the alphabetic characters from the string
    alphabets = [ch for ch in S if ch.isalnum()]
    # Reverse the list of alphabetic characters
    alphabets.reverse()
    # Rebuild the string
    result = []
    for ch in S:
        if ch.isalnum():
            result.append(alphabets.pop(0))  # Replace alphabet with the reversed one
        else:
            result.append(ch)  # Keep special characters unchanged
    # Join the list back to a string
    return ''.join(result)
# Get input from the user
S = input("Enter a string with special characters: ")
# Call the function and print the result
print("Reversed string:", reverse_string(S))
