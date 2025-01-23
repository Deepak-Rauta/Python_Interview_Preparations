def find_second_smallest(arr):
    # First remove duplicates and sort the array
    unique_array = sorted(set(arr))
    if len(unique_array) < 2:
        return None
    return unique_array[2]
arr = [10, 30, 40, 25, 70]
result = find_second_smallest(arr)
print(result)