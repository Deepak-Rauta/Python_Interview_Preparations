#  Find the Index of the First Occurrence in a String

class Solution:
    def FirstOcc(self, haystack, needle):
        return haystack.find(needle)
    
Haystack = "sadbutsad"
Needle = "sad"
solution_instance = Solution()
print(solution_instance.FirstOcc(Haystack, Needle))