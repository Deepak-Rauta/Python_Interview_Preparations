class Solution:
    def Median_Sorted(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return float(merged[n // 2 - 1] + merged[n // 2])/ 2.0
nums1 = [1, 3]
nums2 = [2]
solution_instance = Solution()
print(solution_instance.Median_Sorted(nums1, nums2))