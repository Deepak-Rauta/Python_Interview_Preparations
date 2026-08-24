from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        # Handle the edge cases
        if len(s1) > len(s2):
            return False
        
        # We solve this problem using HashMap + Fixed window
        # First initialize our first window candidate
        counter_s1 = Counter(s1)
        window = Counter()
        left = 0

        for right in range(len(s2)):
            # Add the element
            window[s2[right]] += 1
            # Now check if the window is equal to len(s1) or not?
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                # Now, check if the left window is equal to zero or not
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            # Now compare the window vs counter_s1
            if window == counter_s1:
                return True

        return False 

s1 = "ab"
s2 = "eidbaooo"

obj = Solution()
print(obj.checkInclusion(s1, s2))


