class Solution:
    def Findmajority(self, nums):
        # Take a empty dictionary
        count_dict = {}
        # Majority condition 
        n = len(nums) // 2 # Based on the example majority element must occer > that number 
        for num in nums:
            count_dict[num] = count_dict.get(0, num) + 1
            if count_dict[num] > n:
                return num
numbers = [3, 2, 3]
obj = Solution()
result = obj.Findmajority(numbers)
print(result)


# Solution:-2
class Solution:
    def findMajority(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

numbers = [2, 2, 1, 1, 1, 2, 2]
obj = Solution()
print(obj.findMajority(numbers))