# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

class Solution:
    def RoamnToInt(self, s):
        roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
        total = 0
        previous_value = 0
        for char in reversed(s):
            current_value = roman_values[char]
            if current_value < previous_value:
                total -= current_value
            else:
                total += current_value
            current_value = previous_value
        return total
str = "LVIII"
obj = Solution()
print(obj.RoamnToInt(str))
