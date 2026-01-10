def add_item(item, box=[]): # Dangerous: Default argument is created ONCE at compile time
    box.append(item)
    return box

# Test 1
print(add_item("Apple"))
# Test 2 (Unexpected behavior!)
print(add_item("Banana")) # <-- It remembered the previous state!

# The Fix (Problem Solving Pattern): Always use None as a default for mutable types.
def add_items(item, box=None):
    if box is None:
        box=[]  # Creates a NEW list every time the function runs
    box.append(item)
    return box
print(add_items(["Apple", "Banana", "Orange"]))


# The Loop Way (Slower & Verbose):
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    squares.append(n ** 2)

# The List Comprehension Way (Faster & Pythonic):
squares = [n**2 for n in nums]

import sys
# List Comprehension (Creates the whole list in memory)
my_list = [x for x in range(10)]
print(f"List Memory: {sys.getsizeof(my_list)} bytes") 


# Generator Expression (Uses parentheses instead of brackets)
my_gen = (x for x in range(10000))
print(f"Generator Memory: {sys.getsizeof(my_gen)} bytes")


"""4. Problem Solving Challenge: "The Matrix Flattening"
This exercise combines mutability logic with list comprehensions.

Problem: You have a 2D matrix (a list of lists). You need to flatten it into a single list, but only keep the even numbers."""

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for row in matrix:
    for num in row:
        if num % 2 == 0:
            result.append(num)
print(result)

# Approach 2: Advanced List Comprehension (Pro Level)
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)


"""Round 1: The "Mutable Reference" Trap
Interviewer's Context: "We are building a game board (a matrix). I wrote this code to initialize a 3x3 grid with zeros, and then I tried to place a player 'X' at the top-left corner."""

# Step 1: Create a row of three zeros
row = [0, 0, 0]

# Step 2: Create a grid by repeating that row 3 times
grid = [row] * 3 

# Step 3: Place 'X' at (0, 0)
grid[0][0] = 'X'

print(grid)

"""Why? This is the Reference Trap.

When we did grid = [row] * 3, Python didn't copy the list [0,0,0] three times.

It copied the reference (the pointer) to the row object three times.

grid[0], grid[1], and grid[2] all point to the exact same list object in memory.

Modifying one modifies them all."""

# How to fix it (The Problem Solving way): Use a List Comprehension to create a new list for every row.
grid = [[0]*3 for _ in range(3)]
print(grid)  # # The comprehension runs 3 times, creating 3 DISTINCT list objects.


"""Round 2: The "Conditional Logic" Coding Problem
Interviewer's Context: "I have a list of user IDs. Some are valid (integers), some are messy strings. I need you to clean this data."

The Problem: Given: data = [10, "20", "invalid", 30, "40", "error"] Task: Create a new list containing only the numbers (convert strings to integers where possible). Ignore non-numeric strings.

Constraint: You must use a List Comprehension. No standard for loops."""

data = [10, "20", "invalid", 30, "40", "error"]
result = [int(x) for x in data if str(x).isdigit()]
print(result)
# str(x).isdigit() checks if it looks like a number.

"""Round 3: The "Memory Hog" Optimization
Interviewer's Context: "We need to calculate the sum of squares for 1 billion numbers. My server keeps crashing with a MemoryError."""

# This code crashes
# nums = [x**2 for x in range(10**9)]
# print(sum(nums))
# when i run the above code it will give me KeyboardInterrupt Error 
"""This error does not mean your code had a syntax bug. It means you (or your IDE) manually stopped the program (usually by pressing Ctrl+C or the "Stop" button)."""

"""The Request: You asked Python to calculate 1 Billion squared numbers.

The Problem: Because you used square brackets [] (List Comprehension), Python tried to calculate ALL 1 billion numbers and store them in RAM at the exact same time.

The Math: A Python integer is about 28 bytes.$1,000,000,000 \times 28 \text{ bytes} \approx 28 \text{ GB of RAM}$.

The Freeze: Your computer likely ran out of fast RAM and started using your hard drive as "fake RAM" (swapping). This made your computer extremely slow or unresponsive, forcing you to kill the process."""


# 3. The Fix: Use a Generator
# To fix this, we change the brackets [] to parentheses ().

nums = (x**2 for x in range(10**9))
# now try to loop through a few
import itertools
# Print just the first 5 to prove it works instantly
for n in itertools.islice(nums, 5):
    print(n)

"""Why this works: The Generator () does not calculate 1 billion numbers. It creates a tiny object that knows how to calculate them. It only calculates the number when you ask for it, one by one. This is called Lazy Evaluation."""

"""itertools is a built-in Python module that provides a set of tools for handling iterators (loops) efficiently. Think of it as a "Power Tool Kit" for loops.

Specifically, itertools.islice() solves a major limitation of Generators."""
# 1. The Problem: Generators Cannot be Sliced
# In Python, if you have a List, you can slice it easily:
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[0:3]) # Output: [0, 1, 2] -> EASY

# But if you have a Generator (which saves memory), you cannot slice it because the items don't exist yet!
my_gen = (x for x in range(100))
# print(my_gen[0:3]) 
# TypeError: 'generator' object is not subscriptable
# Python says: "I can't jump to index 3 because I haven't calculated index 0, 1, and 2 yet!"


# Deep Dive: "DSA" Problem Solving Application
"""Problem: Intersection of Two Arrays Given two lists, nums1 and nums2, return an array of their intersection (items present in both). Each element in the result must be unique."""

class Solution:
    def Interseaction(self, nums1, nums2):
        res = []
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2 and n1 not in res:
                    res.append(n1)
        return res
nums1 = [1, 2, 3, 4, 5]
nums2 = [2, 3, 6, 1, 8]

obj = Solution()
print(obj.Interseaction(nums1, nums2))
# # Time Complexity: O(n*m) - Very Slow

"""The "Pythonic/Efficient" Solution (Using Sets & Efficiency): We use set() (Mutable, but O(1) lookup speed) and list comprehension logic concepts."""

class Solution:
    def EffecientSolution(self, nums1, nums2):
        # convert one to a set for O(1) lookups
        seen = set(nums1)
        return list(set(n for n in nums2 if n in seen))
        # OR simpler:
        # return list(set(nums1) & set(nums2)) -- Set intersection operator
nums1 = [1, 2, 3, 4, 5]
nums2 = [2, 3, 5, 1, 8]

obj = Solution()
print(obj.EffecientSolution(nums1, nums2))

