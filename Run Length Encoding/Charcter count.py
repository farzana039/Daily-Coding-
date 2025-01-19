def encode(s):
    if not s:
        return ""  
    encoded_string = ""  
    count = 1  
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  
        else:
            encoded_string += s[i - 1] + str(count)
            count = 1  
    encoded_string += s[-1] + str(count)
    return encoded_string  
user_input = input("Enter the string to encode: ")
result = encode(user_input)  
print("Encoded string:", result)  
