# def toggle_elements(n):
#     # First convert the integer to binary
#     binary_representation = bin(n)[2:]
#     # Toggle the bits
#     toggled_binary = ''.join('1' if bit == '0' else '0' for bit in binary_representation)
#     # convert the toggled binary back to the integer
#     toggled_number = int(toggled_binary, 2)
#     return toggled_number
# number = 10
# result = toggle_elements(number)
# print(result)



class Solution:
    def toggle_element(self, n):
        # convert to binary
        binary_representation = bin(n)[2:]
        # Toggle the bit
        toggled_bits = ''.join('1' if bit == '0' else '0' for bit in binary_representation)
        # convert into integer
        toggled_number = int(toggled_bits,2)
        return toggled_number

number = 10
solution_instance = Solution()
result = solution_instance.toggle_element(number)
print(result)    