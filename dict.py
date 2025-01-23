# Dictonary symbol: {}
# Creating empty dictonary we use: empty_dict = {}
# and also we did: empty_dict = dict()

# a dictonary with key-value pairs is represented as {key1: value2, key2: value2}

# Q. Add a key-value pairs to a dictonary
my_dict = {'name': 'Deepak', 'Age': 25}
my_dict['gender'] = 'Female'
print(my_dict)


# Q. Merge two dictonary
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
dict1.update(dict2) # For merging we use update methods 
print(dict1)

# Q. Remove a key from a dictonary
my_dict = {'Name': 'Deepak', 'Age': 22, 'City': 'HYD'}
my_dict.pop('City') # For removing wer use pop methods 
print(my_dict)

# Q. Check if a key exists in a dictonary
my_dict = {'name': 'Deepak', 'Age': 22}
if 'name' in my_dict:
    print('Key-exists')
else:
    print('Key does not exists')

# Q. Iterate through a dictonary
my_dict = {'name': 'Deepak', 'Age': 22, 'City': 'HYD'}
for key, values in my_dict.items(): # For iterate purpose we use .items()
    print(f"{key}: {values}")

# Q. Find the length
my_dict = {'name': 'Deepak', 'Age': 22, 'City': 'HYD'}
print(len(my_dict))

# Q. Get a  Value with a default if the key does not exists
# Retrive the value for the key 'age' from my_dict and its return 30 
my_dict = {'Name': 'Deepak'}
age = my_dict.get('age', 30)
print(age)

# Q. Create a dictonary from two list
keys = ['name', 'age', 'city']
values = ['Deepak', 22, 'HYD']
my_dict = dict(zip(keys, values))
print(my_dict)

# Q. Sort a dictonary by keys
my_dict = {'c': 3, 'b': 2, 'a': 1}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)

# Q. Find the max. values in dictonary
my_dict = {'a': 10, 'b': 20, 'c': 30}
max_key = max(my_dict, key=my_dict.get) # This is used function like max() or min() we want to find a key based on its value in the dictonary
print(max_key)


#################### Tricky Questions ############################

# Q1. Write a program to count the frequency of each character in a given string using a dictionary.
def count_frequency(str):
    dict = {}
    for char in str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
string = 'banana'
result = count_frequency(string)
print(result)


# Q2. Given a list of integers, find the top 2 most frequent elements using a dictionary.

from collections import Counter
num = [20, 30, 50, 60, 10, 50, 20, 50, 90]
freq_key = Counter(num)

# Find the 2 most common elements
top_2 = [items[0] for items in freq_key.most_common(2)]
print(top_2)


# Q3. Given a list of words, group words that have the same set of characters.

from collections import defaultdict

words = ['bat', 'tab', 'cat', 'act', 'tac', 'rat', 'tar']
gerouped_dict = defaultdict(list) # Also sorted version of the words, and the value will be list of words thta share the same values 

for word in words:
    key = "".join(sorted(word)) # Sort the character in the word
    gerouped_dict[key].append(word)

print(list(gerouped_dict.values()))


# defaultdict: Unlike a normal dictionary, if a key does not exist in a defaultdict, it automatically creates a new entry with a default value.
# defaultdict(list) : means that if a key does not exist, it will create an empty list as default value for that key
