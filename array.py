# What is an Array? (Simple Definition)
# An array is a collection of elements:
# 1. Stored in continuous memory

# 2. All elements are of the same data type

# 3. Accessed using an index

# 🔹 Why Arrays Are Important in DSA?

# Almost 80% of DSA problems are based on arrays or use arrays internally.

# Arrays help you:

# Store multiple values efficiently

# Traverse data easily

# Apply patterns like:

# Two pointers

# Sliding window

# Prefix sum

# 01. Array traversal
# By value:-
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num)
print("----------------------------------------------------------------------------------------")

# By index:-
for i in range(len(arr)):
    print(i, arr[i])
print("----------------------------------------------------------------------------------------")

# By both value + index
for i, num in enumerate(arr):
    print(i, num)

print("----------------------------------------------------------------------------------------")

# 3. Basic Array Techniques
# Find maximum/minimum
arr = [1, 2, 3, 4, 5, 6, 7]
max_value = max(arr)
print(max_value)

min_value = min(arr)
print(min_value)

# Manual logic for maximum:-
maximum = arr[0]
for num in arr:
    if num > maximum:
        maximum = num
print(maximum)

# Manual logic for minimum
minimum = arr[0]
for num in arr:
    if num < minimum:
        minimum = num
print(minimum)

# Sum
total = sum(arr)

# Manual logic for sum
total = 0
for num in arr:
    total += num
print(total)

# Reverse
arr.reverse()

# or

arr[::-1]

# Sort
# .sort() method sort the original list inplace and return None.
array = [1, 9, 5, 6, 2]
array_sort = array.sort()
print(array_sort)

# or
# .sorted() method return a new list
array = [2, 4, 1, 7, 6]
sorted_arr = sorted(array)
print(sorted_arr)

# 4. Strings — Core Idea
# A string is a sequence of character
s = "hello"
# Index 
# 01234
s[0]  # h
s[1]  # e
s[2]  # l
s[3]  # l
s[4]  # o
s[-1]  # o

# String are immutable in python
s = "H" + s[1:]
print(s)

# 5. Essential String Operations
s = "hello world"

# Length
print(len(s))

# Lower/Upper
s.lower()
s.upper()

# Remove surrounding spaces
s.strip()

# Split
word = s.split()
print(word)

# Join
# Combine multiple string into one single string
words = ["I", "love", "python"]
result = " ".join(words)
print(result)

# Replace
replaced_string = s.replace("world", "pyhton")
print(replaced_string)

# Check character types

# ch.isalpha()
# ch.isdigit()
# ch.isalnum()
# ch.isspace()

# 6. Slicing — Extremely Important
# General syntax
# arr[start:end:step]
arr = [1, 2, 3, 4, 5, 6, 7]
print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::-1])

# 7. Most Important DSA Patterns

# Traversal:-
# Visit every element exactly once.
array = [10, 20, 30, 40]
for num in array:
    print(num)

# Traversal using index
arr = [10, 20, 30]
for i in range(len(arr)):
    print(i, arr[i])

# traversal by both value and index
arr = [10, 20, 30, 40]
for i, num in enumerate(arr):
    print(i, num)

# Here the time complexity is O(n) because we visit every element one by one.

# 2️⃣ Insertion
# Add a new element
# There are 3 places where we can insert:-
# 1. Beginning
# 2. Middle
# 3. End
# Each behaves differently

# 2️⃣ Insertiont the End
arr = [10, 20, 30]
arr.append(40)
print(arr)

# Here the time complexity is O(1) amortized 
# O(1) amortized means the average cost of an operation is constant O(1) over a long sequence of operations. 

# B) Insert at the Beginning
arr = [20, 30, 40]
# Now, insert 10 can python directly put 10 and index 0?
# the answer is No.
# Because 20 is already exist there everything must move. 
# Move:-
# 20 →
# 30 →
# 40 →
# Then
# 10, 20, 30, 40

# Pyhton code:-
arr = [20, 30, 40]
arr.insert(0, 10)
print(arr)

# Here the time complexity is O(n)because insert at the beginning take O(n)

# C) Insert in the Middle
arr = [10,20,40,50]
arr = [10,20,40,50]

arr.insert(2,30)

print(arr)

# Time Complexity is O(n) because element must shift

# 3️⃣ Deletion 
# Remove an element. 
# Again,

# there are three possibilities.

# Delete from End
arr = [10, 20, 30]
arr.pop()
print(arr)

# Here time complexity is O(1) because nothing is shift. 

# Delete from the beginning
arr = [10, 20, 30, 40]
arr.pop(0)
print(arr)

# Here time complexity is O(n) because everything is shift. 

# Delete from Middle
arr = [10,20,30,40,50]

arr.pop(2)

print(arr)

# Here also time complexity is O(n) because elements are shift.



# Prefix Sum 
# Insteaf of storing 
# 2  4  1  3  5

# Store:-
# 2
# 2 + 4 = 6
# 6 + 1 = 7
# 7 + 3 = 10
# 10 + 5 = 15

# So, prefix sum 
[2, 6, 7, 10, 15]

# Let's see how it builds
# Pyhton code
arr = [2, 4, 1, 3, 5]
# Let's initialize an emty prefix list
prefix = []
running_sum = 0

for num in arr:
    running_sum += num
    prefix.append(running_sum)

print(prefix)


# Cleaner Prefix Sum (Most Used in Interviews)
# Instead of 2, 6, 7, 10, 15
# Most people build 0, 2, 6, 7, 10, 15
# Notice the extra 0 why? because the formual become easier. 

# Build:-
arr = [2, 4, 1, 3, 5]
prefix = [0]

for num in arr:
    prefix.append(prefix[-1] + num)

print(prefix)

# Now the formula is always
# Sum(left,right) = prefix[right+1] - prefix[left]

# Time Complexity:-
# Building Prefix Sum
# O(n)
# One Range Query
# O(1)

"""Where is Prefix Sum Used?

Whenever you read these words in a LeetCode problem:

Range Sum
Continuous Subarray
Sum between indices
Many sum queries
Running total
Cumulative sum

Think immediately:

Can I use Prefix Sum?"""


arr = [1, 2, 3, 4]
# Let's initialize an emty prefix list
prefix = []
running_sum = 0

for num in arr:
    running_sum += num
    prefix.append(running_sum)

print(prefix)