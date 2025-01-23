# 1. Convert a list of keys and values into a dictionary
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]

result = dict(zip(keys, values))
print(result)

# 2. Convert a list into a dictionary with default values
keys = ['name', 'age', 'gender']
result = dict.fromkeys(keys, None)
print(result)

# 3. Convert a list into a dictionary where elements are keys and their indices are values
fruits = ['apple', 'banana', 'cherry']
# using dictonary comprehension with enumerates
result = {fruit: idx for idx, fruit in enumerate(fruits)}
print(result)

# Dictionary comprehensions:
# syntax:
# {key_expression: value_expression for item in iterable if condition}

# Example of find square:-
squares = {x: x**2 for x in range(11)}
print(squares)

# 4. Group elements of a list into a dictionary of frequency counts
numbers = [1,2,2,2,3,3,4,4,4,5,1,7]
dict_freq = {}
for num in numbers:
     dict_freq[num] = dict_freq.get(num, 0)+1
print(dict_freq)

numbers = [1,2,2,3,3,3]
freq_dict = {} # Create the empty dictionary
for num in numbers:
     freq_dict[num] = freq_dict.get(num, 0)+1
print(freq_dict)
    

# 5. Convert a list of tuples into a dictionary
pairs = [('a', 1), ('b', 2), ('c', 3)]
result = dict(pairs)
print(result)