"Write a script that finds the maximum number of consecutive Failures ('F') in a row. If the string is empty or contains no failures, return 0."

class Solution:
    def find_max_failure(self, reports):
        max_streak = 0
        current_streak = 0

        # We loop through every character in the string
        for status in reports:
            if status == 'F':
                current_streak += 1
                # update the record if the current_streak is the new longest
                if current_streak > max_streak:
                    max_streak = current_streak
            else:
                # we hit an 'S' so the streak is broken
                current_streak = 0
        return max_streak
        
reports = "SSFFSFFFS"
obj = Solution()
print(obj.find_max_failure(reports))