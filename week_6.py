"""Phase 1: File I/O & Context Managers (with open...)
1. The Intuition
Imagine you borrow a book from a library. There is a protocol:

Check out (Open) the book.
Read (Process) the content.
Return (Close) the book.

In Python, if you "Check out" a file but forget to "Return" it (close it), you create a "memory leak." The file stays locked, and your operating system runs out of resources."""

# The "Old" Way (Risky):
# f = open("data.txt", "r")
# content = f.read()
# # If an error happens here the line below never run!
# f.close()

"""The "New" Way (Context Managers): Python introduced the with keyword. Think of with as an automatic door closer. No matter what happens inside the room (even if the building sets on fire/an error occurs), the door will close automatically when you leave."""

# Syntax:-
# The patterns: with resource as alias:
# with open("data.csv", "r") as file:
#     data = file.read()
    # As soon as we exist this indentation block, the file closes autometically

"""Modes:

'r': Read (default). Errors if file doesn't exist.

'w': Write. Overwrites existing file or creates a new one.

'a': Append. Adds to the end of the file.

'b': Binary mode (e.g., 'rb' for images/models)."""


"""3. Real-World Data Preprocessing Example
Scenario: You have a large log file (server_logs.txt) where every line is a raw string. You need to read it line-by-line (to avoid crashing RAM with a huge file) and clean the whitespace."""

with open("server_logs.txt", "w") as f:
    f.write(" ERROR: Disk Full \n INFO: Job Started \n")

# Reading and Cleaning
clean_logs = []
with open("server_logs.txt", "r") as f:
    # f is an iterable so we can loop over it directly!
    # This is memory effecient techniques
    for line in f:
        clean_line = line.strip()
        clean_logs.append(clean_line)

print(clean_logs)


"""Level 1 (Basic Read): Write a script that uses a context manager to open a file named dataset.txt in read mode, reads the entire content into a string variable content, and prints it."""

# with open("dataset.txt", "r") as f:
#     content = f.read()
# print(content)

"""Level 2 (Write List): You have a list scores = [88, 92, 79]. Write a block using with to create a new file grades.txt and write each score on a new line."""

scores = [88, 92, 79]
with open("grades.txt", "w") as f:
    for score in scores:
        line_to_write = str(score) + "\n"
        f.write(line_to_write)

# To see the output
# Part 1:- Write the file
scores = [88, 92, 79]
with open("grades.txt", "w") as f:
    for score in scores:
        f.write(str(score) + "\n")

# Part 2:- Read it back to see what happened
print("--- Reading File Content ---")
with open("grades.txt", "r") as f:
    content = f.read()
    print(content)    

"""Level 3 (Append): Assume grades.txt now exists (containing 88, 92, 79). Write a new with block to open the file and append the score 99 to the end."""

with open("grades.txt", "a") as f:
    f.write("99\n")


"""Level 4 (Line Counting - Memory Efficient): Write a function count_lines(filename) that counts the number of lines in a file without reading the whole file into memory at once (i.e., do not use f.read() or f.readlines())."""
def count_lines(filename):
    count = 0
    with open(filename, "r") as f:
        for line in f:
            # We don't even store the line variable; we just count it
            count += 1
    return count

"""Level 5 (Custom Context Manager): Advanced. Create a custom context manager class named Timer using __enter__ and __exit__. It should print "Start" when entering the with block and print "End. Time taken: X seconds" when exiting. Inside the block, put a small sleep command to test it."""

class Timer:
    def __enter__(self):
        # Code that runs when 'with' starts
        print("Timer Started!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Code that runs when 'with' ends (even if error!)
        print("Timer Stopped!")

# Usage
with Timer() as t:
    print("I am doing some work...")


# Phase 2: Exception Handling (try/except)
# The Syntax:
try:
    # 1. Attempt dangerous code here
    result = 10 / 0
except ZeroDivisionError:
    # 2. Run this only if a specific crash happens
    print("You can not divided by Zero!")
except Exception as e:
    # 3. Run this for any other crash
    print(f" Something else went wrong: {e}")
finally:
    # 4. ALWAYS run this
    print("Calculation attempt finished!")


"""Real-World Data Example: You are processing a column of prices. Some are valid ("100"), but some are corrupted ("N/A" or "Free")."""

prices = ["100", "50", "Free", "25", "NA"]
cleaned_price = []
for p in prices:
    try:
        # Try to convert to integer
        clean_p = int(p)
        cleaned_price.append(clean_p)
    except ValueError:
        # If conversion fails (like "Free") handle it gracefully
        print(f"Skipping invalid data: {p}")
print(cleaned_price)

# Using python function
def Processing(prices):
    # Initialize an empty list
    cleaned_price = []
    for price in prices:
        try:
            # Try convert to integer
            clean_price = int(price)
            cleaned_price.append(clean_price)
        except ValueError:
            # If conversion fail (like:- "Free", "NA") handle it gracefully
            print(f"Skipping invalid data: {price}")
    return cleaned_price
prices = ["100", "Invalid", "20", "NA"]
print(Processing(prices))


# Practice Problem:-
"""Level 1 (Basic Net): Write a try/except block that tries to print x (which is not defined). Catch the NameError and print "Variable not defined."""

try:
    print(x)
except NameError:
    print("Variable not defined!")

"""Level 2 (Specific Catch): You have a list my_list = [1, 2, 3]. Write a try/except block that tries to access my_list[10]. Catch the IndexError and print "Index out of range.""" 

my_list = [1, 2, 3]
try:
    my_list[10]
except IndexError:
    print("Index out of range")


"""Level 3 (Dictionary Key): In Data Science, we often parse JSON data that might be missing fields.

Scenario: You have a dictionary user = {'name': 'Alice'}.
Task: Write a block that tries to print user['age']. Catch the KeyError and print "Age not found."""

user = {"name": "Alice"}
try:
    print(user["age"])
except KeyError:
    print("Age not found!")

"""Level 4 (Catching the Message): Sometimes, just knowing that an error happened isn't enough; you want to know why. Python allows you to capture the actual error message generated by the system.

Task: Try to open a file named "ghost.txt" (which does not exist) using with open(...) inside a try block.

Catch: The FileNotFoundError as a variable named e.
Action: Print the system's error message using print(e)."""   

try:
    with open("ghost.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(e)

"""Level 5 (The finally block): The finally block is the cleaner. It runs no matter what happens—whether the code succeeds or fails.

Task: Write a function convert_data(value):
Try: Convert value to an integer and print "Conversion Successful: [number]".
Except: Catch ValueError (if value is not a number) and print "Conversion Failed!".

Finally: Print "Process Finished." (This must appear in both successful and failed cases).
Test it with: convert_data("100") AND convert_data("hello")."""

def convert_data(value):
    try:
        number = int(value)
        print(f"Conversion Successfull: {number}")
    except ValueError:
        print("Conversion Failed!")
    finally:
        print("Process Finished!")
number = "100"
convert_data(number)































