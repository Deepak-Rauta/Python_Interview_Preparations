class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        i = 0
        
        # Handling leading white space
        while i < len(s) and s[i] == ' ':
            i += 1
            
        # Handling sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        
        # Converting the digits
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
            
            # Checking for overflow
            if result * sign > 2**31 - 1:
                return 2**31 - 1
            if result * sign < -2**31:
                return -2**31
        
        return result * sign

# Example usage
solution_instance = Solution()
string = " -042"
result = solution_instance.myAtoi(string)
print(f"The string to integer conversion is: {result}")
