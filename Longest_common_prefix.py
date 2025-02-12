class Solution:
    def LongestCommon(self, strs):
        prefix = strs[0] # Fisrt string is the initial string
        for s in strs[1:]: # compare with all other string
            while not s.startswith(prefix):
                prefix = prefix[:-1] # Till the match remove one one character
                if not prefix:
                    return ""
        return prefix
string = ["flower","flow","flight"]
solution_instance = Solution()
print(solution_instance.LongestCommon(string))
