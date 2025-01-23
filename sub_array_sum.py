def sum_of_all_subarray(arr):
    total_sum = 0
    n = len(arr)
    for start in range(n):
        sub_arr = 0
        for end in range(start, n):
            sub_arr += arr[end]
        total_sum += sub_arr
    return total_sum
arr = [1,2,3,4,5,6]
result = sum_of_all_subarray(arr)
print(result)