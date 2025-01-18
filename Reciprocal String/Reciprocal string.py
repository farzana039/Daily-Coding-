def reciprocal_letters(text):
    # reciprocal of a single character
    def reciprocal(char):
        if char.isalpha():  # Check if the character is alphabetic
            if char.islower():
                return chr(219 - ord(char))  # Lowercase reciprocal
            elif char.isupper():
                return chr(155 - ord(char))  # Uppercase reciprocal
        return char  # Return the character unchanged if not alphabetic
     # Apply the reciprocal function to each character in the text
    return ''.join(reciprocal(char) for char in text)
input_text = input("Enter a string: ")
output_text = reciprocal_letters(input_text)
print("Reciprocal of letters:", output_text)
