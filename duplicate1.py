def find_duplicates(arr):
    duplicates = []
    count = {}
    for num in arr:
        if num in count:
            duplicates.append(num)

        else:
            count[num] = 1    
    return duplicates
#Example to explain
array = [1,2,3,4,5,6,2,4,5,9]
result = find_duplicates(array)
print(result)