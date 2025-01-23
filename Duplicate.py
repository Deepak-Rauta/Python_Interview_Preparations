def find_duplicates(arr):  #we define a function and take array
    duplicates = []  #  Empty list To store the duplicate value
    count = {} # we initialize a empty dictonary count to count each element in the array
    for num in arr:
        if num in count:
            duplicates.append(num)
        else:
            count[num] = 1 # count is the dictonary and num is the current element of the array

    return duplicates
#Example uses
array =[1,2,3,4,2,5,6,3,4]
result = find_duplicates(array) #call the findduplicates function
print(result)





