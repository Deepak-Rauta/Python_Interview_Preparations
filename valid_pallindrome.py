class Solution:
    def Validpalindrome(self, s):
        cleaned_s = ''.join(s.lower() for char in s if char.isalnum())
        left, right = 0, len(cleaned_s)-1
        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -=1
        return True
str = "MADAM"
solution_instance = Solution()
print(solution_instance.Validpalindrome(str))