class Solution:
    def ReverseWord(self, s):
        words = s.split()
        reversed_word = words[::-1]
        return " ".join(reversed_word)
string = "the sky is blue"
solution_instance = Solution()
print(solution_instance.ReverseWord(string))