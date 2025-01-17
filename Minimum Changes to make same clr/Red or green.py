def min_changes_to_same_color(s):
    # Count occurrences of 'R' (red) and 'G' (green)
    red_count = s.count('R')
    green_count = s.count('G')
    # Minimum changes needed to make all letters the same color
    return min(red_count, green_count)
s = input("Enter a string (e.g., 'RRGGR'): ")
min_changes = min_changes_to_same_color(s)
print(f"Minimum number of changes required: {min_changes}")
