def add_and_subtract(n1, n2):
    addition_result = abs(n1 + n2)
    subtraction_result = abs(n1 - n2)
    result = (
        f"Add: {n1} + {n2} = {addition_result}\n"
        f"Sub: {n1} - {n2} = {subtraction_result}"
    )
    return result
try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(add_and_subtract(n1, n2))
except ValueError:
    print("Invalid")
