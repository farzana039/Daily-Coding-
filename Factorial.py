def factorial(n):
    if n < 0:
        return "Invalid"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
try:
    num = int(input("Enter a number: "))
    print(f"Factorial of {num}: {factorial(num)}")
except ValueError:
    print("Invalid")
    
