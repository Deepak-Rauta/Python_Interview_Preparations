# Part 1: *args and **kwargs
"""1. The Intuition
In Python, we usually define functions with a fixed number of arguments (e.g., def add(a, b)). But real-world data is messy and unpredictable. Sometimes you don't know how many inputs you'll get.

*args (Non-Keyword Arguments): Think of this as a "vacuum cleaner" for positional arguments. It sucks up any extra variables you pass into the function and stores them in a Tuple."""

"""**kwargs (Keyword Arguments): This acts like a vacuum for named arguments (key-value pairs). It stores them in a Dictionary."""

"""Note: The names args and kwargs are conventions. You could technically use *data or **config, but * and ** are the operators that do the magic."""

# 2. Real-World Data Science Example
"""Imagine you are building a wrapper function for pandas.read_csv. You want your custom function to always load data with specific logging, but you still want to support all the original arguments of read_csv without re-typing them."""

import pandas as pd
def load_data(filepath, **kwargs):
    print(f"Loading data from {filepath}.......")

    # We pass the 'kwargs' dictionary to pandas.
    df = pd.read_csv(filepath, **kwargs)
    print(f"Loaded shape: {df.shape}")
    return df

# Usage:
# We can pass standard pandas arguments (sep, header, index_col) 
# even though we didn't define them in load_data!
# df = load_data("data.csv", sep="|", header=0, index_col="id")

"""📝 Practice Problems: *args and **kwargs
Please solve the following 5 problems. Start with simple logic and move towards the data manipulation context."""

"""Problem 1 (Easy): Write a function sum_all that accepts any number of integers using *args and returns their sum."""

def sum_all(*args):
    # args comes in as a tuple, eg. (1, 2, 3)
    # We can use the buit-in sum() function directly in it
    return sum(args)
print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40)) # Output: 100

"""Explanation
The * in *args takes all the loose numbers you pass (1, 2, 3) and packs them into a tuple: (1, 2, 3).

Since sum() in Python works on any iterable (like lists or tuples), sum(args) works perfectly."""


"""Problem 2 (Easy-Medium): Write a function format_metadata that accepts a filename (positional argument), and any number of metadata fields as **kwargs (e.g., author="John", date="2023").

It should return a string like this: "File: report.csv | author: John | date: 2023"""

# You are building a function that creates a summary string for a file.
def format_metadata(filename, **kwargs):
    # start the string with the file name
    result_str = f"File: {filename}"

    # Loop through the dictionary item (key-value pairs)
    for key, value in kwargs.items():
       # Append each piece of metadata to the string 
       result_str += f" | {key}: {value}"
    return result_str

# Test case
print(format_metadata("report.csv", author="Deepak", dat="2026", size="2MB"))

"""Problem 3 (Medium): Write a function filter_by_threshold that accepts a threshold value (integer) and any number of integers as *args. It should return a list containing only the numbers from args that are greater than the threshold."""

def filter_by_threshold(threshold, *args):
    # Create an empty list that store the result
    result = []
    for num in args:
        if num > threshold:
            result.append(num)
    return result
print(filter_by_threshold(10, 5, 20, 8, 15, 30))

"""Problem 4 (Medium-Hard): Write a function create_user_profile that requires a username (mandatory positional arg). It should accept any number of **kwargs to build a dictionary of user details. However, if the key is_admin is passed in kwargs, it should strictly default to False regardless of what the user sent. Return the final dictionary.

Goal: Return a dictionary. Security Rule: If the input contains is_admin=True, you must override it and set it to False."""

def create_user_profile(username, **kwargs):
    # 1. Add the mandatory username to the dictionary
    # We treat 'kwargs' just like any other dictionary.
    # It creates a new entry inside the dictionary.
    kwargs['username'] = username

    """The line kwargs['username'] = username is saying: "Open the book, turn to the page labeled 'username', and write down the value held in the variable username."""

    # 2. The Security Rule
    # Check if the user tried to set 'is_admin'
    if 'is_admin' in kwargs:
        # If they did, we overwrite it to False immediately
        kwargs['is_admin'] = False

    # Return the whole dictionary
    return kwargs
# Test Case 1: Standard user
# print(create_user_profile("sam", email="sam@test.com"))

print(create_user_profile("hacker", is_admin=True, city="NY"))




"""Problem 5 (Hard - Data Science Context): Write a function merge_datasets.

It accepts a primary dictionary (representing a dataset row).

It accepts any number of additional dictionaries using *args.

It should merge all dictionaries from args into the primary one.

Constraint: If a key already exists in the primary dictionary, do not overwrite it. Only add new keys."""

def merge_datasets(primary, *args):
    # args is a tuple containing all the other dictionaries
    # Example: args = ( {"name": "Bob", "age": 30}, {"city": "Paris"} )

    # Outer Loop: Go through each extra dictionary in args
    for other_dict in args:

        # # Inner Loop: Go through each key-value pair in that dictionary
        for key, value in other_dict.items():
            # The Constraint: Only add if the key is NOT already there
            if key not in primary:
                primary[key] = value
    return primary

# Test Case
row_main = {"id": 101, "status": "active"}
row_extra1 = {"status": "inactive", "score": 95} # 'status' conflicts!
row_extra2 = {"city": "New York"}

result = merge_datasets(row_main, row_extra1, row_extra2)
print(result)


