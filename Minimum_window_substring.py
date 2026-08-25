from collections import Counter
class Solution:
    def MinWindow(self, s, t):
        # Handling the edge cases
        if len(t) > len(s):
            return ""

        # Initialize the variables
        need = Counter(t)
        required = len(need)
        formed = 0
        left = 0
        window = {}
        min_len = float("inf") # We havn't found any valid window yet.
        min_left = 0 # We need to remember where that window start so i can return the actual substring.

        for right in range(len(s)):
            char = s[right]
            # Add the charcater
            window[char] = window.get(char, 0) + 1
            # Now check character required satisfied or not
            if char in need and window[char] == need[char]:
                formed += 1
            # Shrink while window is valid!
            while formed == required:
                # Update the minimum
                if right - left + 1 < min_len:
                    # Save the minimum length 
                    min_len = right - left + 1
                    min_left = left

                # Remove from the left
                left_char = s[left]
                window[left_char] -= 1

                # Now check requirement is no longer satisfied!
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1 # Because we are doing shrinking 
                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_left:min_left + min_len]

s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
print(obj.MinWindow(s, t))









