# Basic List comprehension

list = [1, 2, 3, 4, 5]
result = [i**2 for i in list]
print(result)


even_no = [10, 15, 20, 25, 30]
even_result = [i for i in even_no if i % 2 == 0]
print(even_no)


# Reverse each string in list
my_lst = ["apple", "Banana", "orange"]
my_result = [lst[::-1] for lst in my_lst]
print(my_result)

# Extract first letter of each word

lst = ["hello", "world", "python"]
my_lt = [i[:1] for i in lst]
print(my_lt)

# Interview level
# Flatten a 2D list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)

# sublist in nested_list → Iterates over each inner list ([1, 2, 3], [4, 5], [6, 7, 8]).
# for num in sublist → Extracts individual elements (num) from each sublist.
# The result is stored in flattened_list.

# Find all number dividible by both 3 and 5
divisible_prob = [num for num in range(1, 51) if num % 3 == 0 and num % 5 ==0]
print(divisible_prob)

# 🔥 3. Convert Fahrenheit to Celsius
fahrenheit = [32, 68, 104, 212]
celcius = [(f-32) * 5/9 for f in fahrenheit]
print(celcius)