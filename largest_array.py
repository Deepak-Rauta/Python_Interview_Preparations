def find_largest_array(arr):
    if not arr:
        return None
    largest = arr[0]
    for elements in arr:
        if elements > largest:
            largest = elements
    return largest
arr = [10, 25, 60, 80, 73]
result = find_largest_array(arr)
print(result)


        # For smallest array
# def find_smallest_array(arr):
#     if not arr:
#         return None
#     smallest = arr[0]
#     for element in arr:
#         if element < smallest:
#             smallest = element
#     return smallest
# arr = [10, 20, 30, 40]
# result = find_smallest_array(arr)
# print(result)


# def count_greater_elements(arr):
#     if not arr:
#         return 0
    
#     count = 1  # The first element is always counted
#     max_so_far = arr[0]  # Initialize max with the first element
    
#     for i in range(len(arr)):
#         if arr[i] > max_so_far:
#             count += 1
#             max_so_far = arr[i]
    
#     return count

# # Example usage
# arr = [7, 4, 8, 2, 9]
# print("Count of elements greater than all preceding elements:", count_greater_elements(arr))

# Largest elememts

def find_largest(arr):
    if not arr:
        return None
    largest = arr[0]
    for element in arr:
        if element > largest:
            largest = element
    return largest
arr = [10, 20, 30, 40]
result = find_largest(arr)
print(result)

