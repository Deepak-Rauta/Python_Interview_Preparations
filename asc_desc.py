def sort_half(arr):
    mid = len(arr) // 2
    # sort the first half in ascending order
    first_half = sorted(arr[:mid])
    # sort the second half in descending order
    second_half = sorted(arr[mid:], reverse = True)
    # Combine both of them 
    return first_half + second_half
arr = [1,10,6,8,9,4]
result = sort_half(arr)
print(result)


