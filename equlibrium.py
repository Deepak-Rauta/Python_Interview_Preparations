def equilibrium_point(arr):
    total_sum = sum(arr) #To store the sum of all elementusing sum() function
    left_sum = 0 # To print the cumulative some
    for i in range(len(arr)):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]
        return -1
    
# Example uses
array = [1,3,5,2,2,7,4]
equilibrium  = equilibrium_point(array) 
if equilibrium != 1:
    print("The equilibrium point is at index", equilibrium) 
else:
    print("There is no equilibrium point in the array")    
