class Solution:
    def threeSum(self, nums):
        # 01. First sort the element
        nums.sort()

        # 02. Initialize an empty result
        result = []

        for i in range(len(nums)):

            # 03. Now skip the duplicate first value
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                # 04. Find the total 
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    # 05. append the result
                    result.append(
                        [nums[i], nums[left], nums[right]]
                    )

                    left += 1
                    right -= 1

                    # Skip duplicates left value
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip the duplicates right value
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:

                    left += 1
                else:

                    right -= 1

        return result

nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(nums))



