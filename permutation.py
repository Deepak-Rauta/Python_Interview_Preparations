from itertools import permutations  # import permutations function from itertools

def get_permutations(input_string):
    # Generate all permutations of the input string
    permuted_strings = [''.join(p) for p in permutations(input_string)] # '' use for empty list and join(p) is a string method
    return permuted_strings

# Get user input
input_string = input("Enter a string: ")

# Get and print permutations
permutations_list = get_permutations(input_string) 
print("Permutations of the string '{}':".format(input_string)) # {} is a palceholder of the value of input_string
# .format(input_string) is used to substitute the actual value of input_string
for permuted_string in permutations_list:
    print(permuted_string)
