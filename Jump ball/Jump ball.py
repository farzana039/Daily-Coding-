def total_distance_traveled(H):
    total_distance = 0  # Initialize total distance to 0
    while H > 0:
        total_distance += H  # Add the upward distance
        H = H // 2  # Calculate the next height (floor(H/2))
        if H > 0:  # If the ball still bounces, add the downward distance
            total_distance += H
    return total_distance
try:
    H = int(input("Enter the initial height of the ball (H): "))
    if H < 0:
        print("Height must be a non-negative integer.")
    else:
        result = total_distance_traveled(H)
        print("Total distance traveled by the ball:", result)
except ValueError:
    print("Invalid input! Please enter an integer.")
