class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        def expandAroundCenter(left: int, right: int) -> str:
            # Expand around the center while the characters are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring (adjust left and right bounds)
            return s[left + 1:right]
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Odd-length palindrome (center is at a single character)
            odd_length_palindrome = expandAroundCenter(i, i)
            # Even-length palindrome (center is between two characters)
            even_length_palindrome = expandAroundCenter(i, i + 1)
            # Update the longest palindrome found
            longest_palindrome = max(longest_palindrome, odd_length_palindrome, even_length_palindrome, key=len)
        
        return longest_palindrome

# Example usage:
solution_instance = Solution()
s = "babad"
result = solution_instance.longestPalindrome(s)
print(result)  # Expected output: "bab" or "aba"
