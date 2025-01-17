def find_bracket_numbers(s):
    stack = []
    result = []
    count = 0  # Counter to assign numbers to brackets
    for char in s:
        if char == '(': #if char is ( ,Stack and result will append "("
            count += 1 #incrementing count value when "(" is found 
            stack.append(count)
            result.append(count)
        elif char == ')':
            if stack:
                result.append(stack.pop()) # popping out the value in stack to result 

    return result
# Taking input from the user
s = input("Enter a string with brackets: ")
output = find_bracket_numbers(s)
print("Bracket numbers:", output)
