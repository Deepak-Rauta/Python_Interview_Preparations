class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        end = 0
        max_len = 0
        seen = set()
        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
                seen.remove(s[start])
                start += 1
                max_len = max(max_len, end - start)
        return max_len
solution_instance = Solution()
s = "abcabcbb"
longest_substring = solution_instance.lengthOfLongestSubstring(s)
print(longest_substring)



# hacker rank problems
def count_string(str, sub_str):
    count = 0
    sub_len = len(sub_str)
    for i in range(len(str) - sub_len + 1):
        if str[i:i+sub_len] == sub_str:
            count += 1
    return count
string = "ABCABCBB"
sub_string = "BCB"
result = count_string(string, sub_string)
print(result)






