# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

class Solution:
    def Convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        # Create the empty rows
        rows = ["" for _ in range(numRows)]
        index = 0
        step = 1
        for char in s:
            rows[index] += char # Add the character to the row at postition to the index
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step # Move down untill the last row & up untill the first row still continue the process
        return "".join(rows)
String = "PAYPALISHIRING"
numRows = 3
obj = Solution()
print(obj.Convert(String, numRows))
