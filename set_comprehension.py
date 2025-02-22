# 3️⃣ Set Comprehension Problems
# ✅ Basic Problems
# Remove duplicates from a list using set comprehension

set_list = [1,2,2,3,4,4,5]
filter_set = set(set_list)
print(filter_set)

# Find unique vowels in a string
input = "education"
vowels = {'a', 'e', 'i', 'o', 'u'}
unique_vowels = {char for char in input if char in vowels}
print(unique_vowels)


# 🔥 Interview-Level Problems
# 3️⃣ Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = set(list1) & set(list2)
print(common_elements)

# 4️⃣ Find unique words in a sentence
sentence = "Python is great and Python is fun"
result = {word for word in sentence.split()}
print(result)

# 5️⃣ Find numbers in a range that are divisible by 4 but not by 6
numbers = {num for num in range(1, 51) if num % 4 == 0 and num % 6 !=0}
print(numbers)