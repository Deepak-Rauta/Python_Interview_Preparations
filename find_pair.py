def find_pairs(arr, target_sum):
    # Dictionary to store numbers and their counts
    num_dict = {}
    # List to store pairs
    pairs = []

    for num in arr:
        # Calculate the required complement for the current number
        complement = target_sum - num
        # Check if the complement is already in the dictionary
        if complement in num_dict:
            pairs.append((complement, num))
        # Add the current number to the dictionary
        num_dict[num] = num_dict.get(num, 0) + 1


    return pairs

# Example usage:
arr = [1, 2, 3, 4, 5]
target_sum = 6
result = find_pairs(arr, target_sum)
print("Pairs with sum", target_sum, ':', result)