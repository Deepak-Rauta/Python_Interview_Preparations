from collections import Counter
def sort_by_frequency(arr):
    # count frequency
    frequency = Counter(arr)
    # sort the elements based on frequency and values
    arr.sort(key = lambda x: (-frequency[x], x))
    return arr
arr = [1,2,2,3,3,5,5,7,8,9,9]
result = sort_by_frequency(arr)
print(result)