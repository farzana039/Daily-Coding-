def is_palindrome(s):
    #Filter only alphanumeric characters and convert to lowercase
    string_after_removing_characters = ''.join(c.lower() for c in s if ('a' <= c.lower() <= 'z') or ('0' <= c <= '9'))
    return string_after_removing_characters == string_after_removing_characters[::-1]  
s=input()
print(is_palindrome(s))

