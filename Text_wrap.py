# import textwrap

# def wrap(string, max_width):
#     return

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

# This code only prove the last substring 
# import textwrap
# def wrap(string, max_width):
#     for i in range(0, len(string), max_width):
#         substring = string[i:i + max_width]
#     return substring
# string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# max_depth = 4
# result = wrap(string, max_depth)
# print(result)


import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max_depth = 4
result = wrap(string, max_depth)
print(result)
