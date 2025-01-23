#User function Template for python3


class Solution: #code define a class name solution
    def missingNumber(self,arr,n): #it contain two parameter arr, integer(n)
        # code here
        expected_sum = (n*(n+1))//2
        
        #calculate the sum of the given array
        array_sum = sum(arr)
        
        # The missing element is the difference between the expected sum and the array
        missingNumber = expected_sum - array_sum
        
        return missingNumber
        
# Example uses:
arr = [1,2,3,5]
n = len(arr) + 1 # N is one more then the array size
# create an instance of the solution class
solution_instance = Solution()

#call the missingNumber method on the instance
result = solution_instance.missingNumber(arr, n)
print(result)


# Method-2

# def FindMissingNumber(arr):
#     n = 4
#     expected_sum = (n*(n+1))//2
#     actual_sum = sum(arr)
#     missing_number = expected_sum - actual_sum
#     return missing_number
# array = [i for i in range(1, 5) if i != 3]
# print(FindMissingNumber(array))

