def find_leader(arr):
    leader = [] # To store the leader element
    max_right = arr[-1]
    leader.append(max_right)
    for i in range(len(arr)-2,-1,-1:):
        if arr[i]>max_right:
            max_right = arr[i]
            leader.append(max_right)
    leader.reverse()
    return leader
#Example uses
array = [3,8,2,10,5]
leader_element = find_leader(array)
print("leader element in the array is", leader_element)        