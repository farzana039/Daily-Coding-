def calculate_ratios(arr):
    n = len(arr)
    positives = sum(1 for x in arr if x > 0) # count +ve value
    negatives = sum(1 for x in arr if x < 0)# count -ve value
    zeros = sum(1 for x in arr if x == 0)#count 0 values
    # Calculating ratios of +ve,-ve,0
    positive_ratio = positives / n
    negative_ratio = negatives / n
    zero_ratio = zeros / n
    # Return ratios with 6 decimal places
    return f"{positive_ratio:.6f}", f"{negative_ratio:.6f}", f"{zero_ratio:.6f}"
arr = [1, -2, 3, 0, -5, 0, 6]
positive_ratio, negative_ratio, zero_ratio = calculate_ratios(arr)
print("Positive Ratio:", positive_ratio)
print("Negative Ratio:", negative_ratio)
print("Zero Ratio:", zero_ratio)
