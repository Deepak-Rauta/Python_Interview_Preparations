def is_palindrome(word):
    return word == word[::-1]
def longest_palindrome(arr):
    longest = " "
    for word in arr:
        if is_palindrome(word) and len(word) > len(longest):
            longest = word
    return longest if longest else "No palindrome found"
arr = ["racecar", "hello", "level", "world", "deified", "test"]
result = longest_palindrome(arr)
print(f"The longest palindrome in the array is: {result}")





# p-2
def is_palindrome(s):
    return s == s[::-1]

def palindrome_substrings(string):
    palindromes = []
    n = len(string)
    
    # Check all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                palindromes.append(substring)
    
    return palindromes

# Example usage
string = "ababa"
result = palindrome_substrings(string)
print("Palindrome substrings:", result)


# Normal palindrome problems
class Solution:
    def IsPalindriome(self, x):
        return str(x) == str(x)[::-1]

string = 121
obj = Solution()
print(obj.IsPalindriome(string))
                                