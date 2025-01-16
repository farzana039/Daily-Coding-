array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]
union_set = set()# Create an empty set to store the union
for element in array1: # Add all elements from array1 to the set
   union_set.add(element)
for element in array2: # Add all elements from array2 to the set
   union_set.add(element)
print("Union:", union_set)
