def machine_time(weight, water_level):
   if weight < 0:
        return "Invalid"
   elif weight == 0:
        return "Time Estimated: 0 minutes"
   elif weight > 7000:
        return "Overloaded"
   else:
        if water_level == 'L':
            if 0 < weight <= 2000:
                return "Time Estimated: 25 minutes"
            else:
                return "Invalid"
        elif water_level == 'M':
            if 2001 <= weight <= 4000:
                return "Time Estimated: 35 minutes"
            else:
                return "Invalid"
        elif water_level == 'H':
            if 4001 <= weight <= 7000:
                return "Time Estimated: 45 minutes"
            else:
                return "Invalid"
        else:
            return "Invalid"
try:
    weight = int(input("Enter the weight of the clothes: "))
    water_level = input("Enter the water level: ").strip().upper()
    print(machine_time(weight, water_level))
except ValueError:
    print("Invalid")
