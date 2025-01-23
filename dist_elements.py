def find_distinct(arr):
    # Use a set to store the distinct elements
    distinct_elements = set(arr)
    # count the distinct elements
    return len(distinct_elements)
arr = [1,2,2,3,4,4,5,6,7,7,9,9]
result = find_distinct(arr)
print(result)