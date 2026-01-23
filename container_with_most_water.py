"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""

class Solution:
    def maxArea(self, height):
        # 01: Initialize the pointers
        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:
            # 02: Find the width
            width = right - left

            # 03: Find the height
            h = min(height[left], height[right])

            # 04: Find the maximum area
            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
obj = Solution()
print(obj.maxArea(heights))


# Interview trap

"""Why do you move the pointer associated with the smaller height?

(For example, if height[left] is 3 and height[right] is 8, you move left. Why didn't you try moving right to see if there was a better match for the 3?)"""
# Answer:-
"""Because the area is limited by the shorter height, moving the taller pointer cannot increase the area. Only moving the smaller pointer gives a chance to find a taller line and increase the are"""