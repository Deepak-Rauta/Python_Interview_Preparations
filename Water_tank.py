class Solution:
    def Max_water(self, height):
        left, right = 0, len(height)-1
        max_water = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_water = max(max_water, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
height = [1,8,6,2,5,4,8,3,7]
solution_instance = Solution()
print(solution_instance.Max_water(height))

class Solution:
    def MaxWater(self, height):
        left, right = 0, len(height)-1
        max_water = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_water = max(max_water, area)
            
