def find_password(n, S):
    if S > 9 * n or S < 0: #initial condition
        return "Invalid input: No such password exists."
    password_digits = [] #empty list to store array
    for i in range(n):
        digit = min(9, S)# Take the  possible value for this digit
        password_digits.append(str(digit))
        S -= digit  # Subtract this digit from the sum
    # Join the digits to form the password
    password = "".join(password_digits)
    return password
try:
    n = int(input("Enter the number of digits in the password: "))
    S = int(input("Enter the sum of the digits in the password: "))
    result = find_password(n, S)
    print("The password is:", result)
except ValueError:
    print("Invalid input! Please enter valid integers.")
