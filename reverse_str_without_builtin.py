# With out using in-built function
def is_reverse(str):
    reversed_str = ''
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str
my_string = "Deepak"
result = is_reverse(my_string)
print(result)