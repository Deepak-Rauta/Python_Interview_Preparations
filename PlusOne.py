# class Solution:
#     def Plusone(self, digits):
#         num = int("".join(map(str, digits)))
#         num += 1
#         return [int(digit) for digit in str(num)]
# Digit = [1, 2, 3]
# obj = Solution()
# print(obj.Plusone(Digit))



# Plus one problem with manual carry methods

class Solution:
    def PlusOne(self, digits):
        # Find the length
        n = len(digits)
        # Iterate backwords from the last index
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9 than put 0 and carry 1
            digits[i] = 0
        return [1] + digits

digits = [9, 9, 9]
obj = Solution()
print(obj.PlusOne(digits))