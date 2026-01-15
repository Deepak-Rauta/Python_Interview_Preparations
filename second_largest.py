"""The Task: Given an array, return the second largest distinct element. The Catch: Try to do this in a single pass (loop through the array only once)."""

 
class Solution:
    def getSecondLargest(self, arr):
        # Initialize with negative infinity so any number in the array is larger
        largest = float('-inf')
        second = float('-inf')
        
        for num in arr:
            if num > largest:
                # Found a new maximum! 
                # The old 'largest' becomes the new 'second'
                second = largest
                largest = num
            elif num > second and num != largest:
                # Found a number smaller than 'largest' but bigger than 'second'
                second = num
                
        # Handle case where no second largest exists (e.g., array with all same elements)
        if second == float('-inf'):
            return None 
            
        return second

# Test
sol = Solution()
print(sol.getSecondLargest([12, 35, 1, 10, 34, 1]))  # Output: 34
