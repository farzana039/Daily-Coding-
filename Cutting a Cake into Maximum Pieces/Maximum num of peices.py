def max_cake_pieces(n):
    # Use the formula to calculate maximum pieces
    return (n * (n + 1)) // 2 + 1
try:
    n = int(input("Enter the number of cuts: "))
    if n < 0:
        print("The number of cuts cannot be negative.")
    else:
        result = max_cake_pieces(n)
        print(f"The maximum number of pieces with {n} cuts is: {result}")
