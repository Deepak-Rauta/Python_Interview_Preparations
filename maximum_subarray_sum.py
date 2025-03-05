class Solution:
    def Max_subarray(self, arr):
        max_current = max_global = arr[0]
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            max_global = max(max_current, max_global)
        return max_global
    
arrays = [-2,1,-3,4,-1,2,1,-5,4]
solution_instance = Solution()
print(solution_instance.Max_subarray(arrays))
