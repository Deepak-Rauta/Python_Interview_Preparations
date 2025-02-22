# ✅ Basic Problems
# Create a dictionary from a list

letters = ['a', 'b', 'c']
letter_dict = {letters[i]: i+1 for i in range(len(letters))}
print(letter_dict)

# ✅ Explanation:
# We loop through letters using range(len(letters)).
# letters[i] is the key, and i + 1 is the value.

# 🔥 2. Square of numbers in a dictionary
# Problem: Given [1, 2, 3, 4, 5], generate {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

numbers = [1,2,3,4,5]
sq_num = {num: num ** 2 for num in numbers}
print(sq_num)

# 🔥 3. Count character frequency in a string
# Problem: Input "hello", output {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

word = "hello"
char_frequency = {char: word.count(char) for char in word}
print(char_frequency)

# 🔥 Interview-Level Problems

# 🔥 1. Swap Keys and Values in a Dictionary
# Problem: Given {'a': 1, 'b': 2, 'c': 3}, return {1: 'a', 2: 'b', 3: 'c'}
original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {value: key for key, value in original_dict.items()}
print(swapped_dict)

# 🔥 2. Filter Dictionary Based on Values
# Problem: Given {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}, return students with marks ≥ 80.

students = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
filtered_result = {name: marks for name, marks in students.items() if marks >= 80}
print(filtered_result)

#🔥 3. Create a Dictionary from Two Lists
# Problem: Given keys = ['name', 'age', 'city'] and values = ['John', 25, 'New York'], return {'name': 'John', 'age': 25, 'city': 'New York'}.
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
combined_list = dict(zip(keys, values))
print(combined_list)