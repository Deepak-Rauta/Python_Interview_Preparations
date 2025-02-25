from collections import Counter

class Solution:
    def ConcatAllWords(self, s, words):
        word_len = len(words[0]) # each word length
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []

        for i in range(len(s) - total_len + 1):
            sub = s[i:i + total_len]
            temp_word = [sub[j:j + word_len] for j in range(0, total_len, word_len)]
            if Counter(temp_word) == word_count:
                result.append(i)
        return result
s = "barfoothefoobarman"
words = ["foo","bar"]
solution_instance = Solution()
print(solution_instance.ConcatAllWords(s, words))


