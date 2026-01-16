# A list is an Iterable, but NOT an Iterator
my_list = [1, 2, 3, 4, 5]

# This would crash: next(my_list) -> TypeError: 'list' object is not an iterator
# We must get the Iterator (the bookmark) first
my_iterartor = iter(my_list)  # Calls my_list.__iter__()
print(next(my_iterartor))
print(next(my_iterartor))
print(next(my_iterartor))
print(next(my_iterartor))
print(next(my_iterartor))

# 2. Generators & The yield Keyword
"""Creating a class with __iter__ and __next__ is verbose (boilerplate code). Generators are a simple way to create Iterators using functions.

The Keyword: If a function contains the yield keyword, Python automatically flags it as a generator.

The Magic: When you call a generator function, it doesn't run the code. It returns a generator object (which is an iterator)."""

"""Execution:

When you call next() on it, the code runs until it hits yield.

It pauses execution, saves the entire state (variables, local scope), and returns the yielded value.

The next next() resumes exactly where it left off."""

def simple_generator():
    print("Starting.....")
    yield 1
    print("Resuming.....")
    yield 2
    print("Done.....")
gen = simple_generator()
print(next(gen))
print(next(gen))


"""Part 2: Real-World Data Science Example
The "Poor Man's" PyTorch DataLoader
Imagine you have a CSV file massive_data.csv with 1 billion rows. You cannot open this in Pandas (pd.read_csv). You must stream it.

Here is how we use a Generator to read chunks of data (batches) for training."""

import time

# Mocking a massive dataset as a list of numbers
massive_dataset = range(100)

def data_loader(data, batch_size):
    """
    Yields mini-batches of data

    """
    for i in range(0, len(data), batch_size):
        # Slice the batch
        batch = data[i : i + batch_size]

        # Simulate heavy preprocessing (e.g., image resizing)
        preprocessed_batch = [x * 2 for x in batch]

        
        # PAUSE here and give the batch to the training loop
        yield preprocessed_batch

# Usage in a Training Loop
loader = data_loader(massive_dataset, batch_size=4)
print("Starting training...")

for batch_idx, batch in enumerate(loader):
    # The generator only processes the next 4 items when the loop asks for them
    print(f"Batch {batch_idx}: {batch}")
    # train_model(batch) ...


# Step-by-Step Execution
# 1. Setup (Lines 1-18)
massive_dataset = range(100) 
loader = data_loader(massive_dataset, batch_size=4)
"""massive_dataset = range(100) 
loader = data_loader(massive_dataset, batch_size=4)"""
# 2. The Request (Line 21)
"""The for loop hits the loader.

It implicitly calls next(loader). It effectively yells: "Hey Generator, give me the first item!"

3. The Generator Wakes Up (Lines 7-10)
The generator starts running from line 1.

It enters its own loop: for i in range(0, 100, 4).

First pass (i = 0):

It slices data[0 : 4] (items 0, 1, 2, 3).

It multiplies them by 2: [0, 2, 4, 6]."""
# 4. The Yield (Line 18)
# yield processed_batch
# 5. Main Loop Processing (Line 23)
# print(f"Batch {batch_idx}: {batch}")


"""The variable batch now holds [0, 2, 4, 6].

The main loop prints it.

The code processes this batch (e.g., trains a neural network).

Memory: Once this iteration finishes, that list [0, 2, 4, 6] is thrown away (garbage collected) to free up RAM.

6. The Next Request
The main for loop loops around. It calls next(loader) again. "Hey, give me the next one!"

7. Generator Resumes
The generator wakes up exactly at Line 18 (where it paused).

It finishes that iteration of its internal loop.

It loops again! Now i increments to 4.

It slices data[4 : 8], processes them.

It hits yield again. Pauses. Hands back data.

Visualizing the "Handshake"
This cycle repeats until i reaches 100.

Main: "Next?"

Gen: (Wakes up, cooks batch 1, Pauses) "Here."

Main: (Eats batch 1) "Next?"

Gen: (Wakes up, cooks batch 2, Pauses) "Here."""



"""Basic Yield: Write a generator function count_up_to(n) that yields numbers from 1 to n."""
def count_up_to(n):
    # Loop from 1 up to n (range stops one step before the end, so we use n+1)
    for i in range(1, n+1):
        yield i

# create the generator object
counter = count_up_to(3)
print(next(counter))
print(next(counter))
print(next(counter))

"""Even Numbers Generator
Write a generator even_numbers(n) that yields all even numbers from 1 to n."""

def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i

even_count = even_numbers(5)
print(next(even_count))
print(next(even_count))


"""Odd Numbers Generator
Write a generator odd_numbers(n) that yields all odd numbers from 1 to n."""

def odd_number(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            yield i 
odd_count = odd_number(3)
print(next(odd_count))
print(next(odd_count))

"""Countdown Generator
Write a generator count_down(n) that yields numbers from n down to 1."""

def count_down(n):
    while n >= 1:
        yield n
        n -= 1

cd = count_down(5)
print(next(cd))

"""Square Numbers Generator
Write a generator squares(n) that yields squares of numbers from 1 to n."""
def squares(n):
    for i in range(1, n+1):
        yield i ** 2

sq = squares(4)
print(next(sq))
