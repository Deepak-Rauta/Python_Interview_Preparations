class Solution:
    def ReverseString(self, str):
        reversed_string = ""
        for char in str:
            reversed_string = char + reversed_string
        return reversed_string
string = "Hello"
obj = Solution()
print(obj.ReverseString(string))