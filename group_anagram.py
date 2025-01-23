from collections import defaultdict
class Solution:
    def find_anagram(self, strs):
        group_anagrams = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            group_anagrams[sorted_word].append(word)
        return list(group_anagrams.values())
solution_instance = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution_instance.find_anagram(strs)
print(result)
