def find_cars_and_bikes(vehicles, wheels):
    # Check for invalid input
    if wheels % 2 != 0 or wheels < 2 * vehicles or wheels > 4 * vehicles:
        return "Invalid input: Please check the numbers of vehicles and wheels."
    cars = (wheels - 2 * vehicles) // 2 # Calculate number of cars and bikes
    bikes = vehicles - cars
    return cars, bikes
try:
    vehicles = int(input("Enter the number of vehicles: "))
    wheels = int(input("Enter the number of wheels: "))
    result = find_cars_and_bikes(vehicles, wheels)
    if isinstance(result, str):
        print(result)  
    else:
        cars, bikes = result
        print(f"Number of cars: {cars}")
        print(f"Number of bikes: {bikes}")
except ValueError:
    print("Invalid input: Please enter valid integers.")
