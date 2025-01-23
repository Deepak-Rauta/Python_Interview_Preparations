# python program to find the first non-repeating character
def find_first_non(str):
    frequency = {}
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    # Now find the first non repeating character
    for char in str:
        if frequency[char] == 1:
            return char
        return None
my_string = "Hello world"
result = find_first_non(my_string)
print(result)