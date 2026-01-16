"""Concept: Python Decorators
1. The Intuition (From Zero)
Imagine you have a painting (your function). You want to put it in a frame. The frame doesn't change the painting itself; it just surrounds it, perhaps adding a glass cover for protection or a fancy border for aesthetics.

In Python, a Decorator is that frame.

The Input: A function.

The Action: It wraps the function inside another function (the "wrapper").

The Output: A new, enhanced function that contains the original logic plus some "before" and "after" code."""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

# We manually 'wrap' the function
say_hello = my_decorator(say_hello)
"""The "Syntactic Sugar" Way (The @ symbol): Python gives us the @ shortcut to do the exact same thing as above."""
@my_decorator
def say_hello():
    print("Hello!")


def add(a, b):
    return a + b
f = add
print(f(2, 3))  # 5
# 👉 This is the only reason decorators are possible.

# 2. Function inside a function (Closure intuition)
def outer():
    def inner():
        print("Hello from inner")
    inner()

# Now the important part:
def outer():
    def inner():
        print("hello")
    return inner
f = outer()
f()

"""🔑 Key idea:
inner remembers the environment where it was created.

This is called a closure."""

"""PART 2️⃣ — What is a Decorator?
Definition (Interview-ready)

A decorator is a function that takes another function, adds extra behavior, and returns a new function, without modifying the original code."""

# Example: Logging function calls
def my_decorator(func):
    def wrapper():
        print("Function is about to run")
        func() # so inside my_decorator func = say_hello()
        print("Function finished")
    return wrapper
def say_hello():
    print('hello')

say_hello = my_decorator(say_hello) # calling my_decorator and passing the function say_hello as an arguments 
say_hello()

"""📌 Important:
wrapper knows that func = say_hello"""

# PART 3️⃣ — Using @decorator syntax
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print('Hi')

greet()

"""🔹 What @my_decorator REALLY does

@my_decorator
def greet():
    print('Hi')

    Is exactly the same as:
    def greet():
    print('Hi')

greet = my_decorator(greet)

"""

"""So now:
greet → points to wrapper
Original greet() is stored inside wrapper as func
🔹 When you call:
greet()
Python actually runs:
wrapper()
"""

# 🔥 INTERVIEWER UPGRADE (VERY IMPORTANT)
"""An interviewer may now ask:

❓ “What if the function has arguments?”

Your current code ❌ will FAIL for this:"""


# ✅ Interview-Ready Version
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet():
    print("Hi.....")
greet()

"""🔥 PROFESSIONAL INTERVIEW UPGRADE
❓ Interviewer might ask:

“Can you show which function is being executed?”"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet():
    print("Hello.....")
greet()

"""IMPORTANT INTERVIEW DETAIL (VERY COMMON QUESTION)
❓ “What is the problem with this decorator?”

Answer:
It hides the original function’s metadata (name, docstring)

Fix using functools.wraps (🔥 MUST KNOW)"""
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Copies the original function’s details into wrapper
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)
    return wrapper
@my_decorator
def greet():
    print("Hello.....")
greet()

"""What @wraps(func) REALLY does (VERY IMPORTANT)

It copies:
Function name (__name__)
Docstring (__doc__)
Help info
Metadata (used by FastAPI, ML tools, debuggers)"""


"""Problem 1: The Basic Wrapper
Goal: Understand basic syntax and the wrapper structure.
Task: Write a decorator named @simple_logger.
It should print "Start Processing..." before the decorated function runs.
It should print "Processing Complete." after the decorated function runs.
Apply it to a function load_data() that simply prints "Loading CSV file..."."""

def simple_logger(func):
    def wrapper():
        print("Start Preprocessing...")
        func()
        print("Preprocessing Complete.")
    return wrapper

@simple_logger
def Loading():
    print("Loading CSV File...")
Loading()

"""Problem 2: Handling Arguments (*args, **kwargs)
Goal: Decorators must be flexible. Most data science functions take parameters (datasets, hyperparameters, etc.).
Task: Write a decorator named @inspect_args.
It should print the arguments passed to the function before it runs.
It needs to handle both positional arguments (args) and keyword arguments (kwargs).
Apply it to a function train_model(model_type, epochs=5) which prints "Training..."""

from functools import wraps
def inspect_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Print the arguments captured
        print(f"Arguments: {args} {kwargs}")

        # Pass the arguments to the actual function
        return func(*args, **kwargs)
    return wrapper

@inspect_args
def train_model(model_type, epoch=5):
    print(f'Training {model_type} for {epoch} epochs...')

train_model("XGBoost", epoch=10)



"""Problem 3: Modifying the Return Value
Goal: Understand that decorators can intercept and change what a function outputs.
Task: Write a decorator named @standardize_output.
The decorated function will return a list of numbers (e.g., [100, 200, 300]).
The decorator should take that result and normalize it (scale the values between 0 and 1).
Formula: value / max_value (Assume max_value is the largest number in the list).
Apply it to a function get_predictions() that returns [10, 20, 50, 100]."""

# return-value interception
from functools import wraps
def standardize_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Excecute the function to get the raw data
        # 3️⃣ Capturing return value
        raw_data = func(*args, **kwargs)
        # Modify the data (Normalization logic)
        if not raw_data: # Handling empty output (edge case)
            return []
        # 5️⃣ Normalization logic
        max_value = max(raw_data)
        normalized_data = [x / max_value for x in raw_data]

        # Return the new modified data
        return normalized_data
    return wrapper

@standardize_output
def get_predictions():
    return [10, 20, 50, 100]
print(get_predictions())

"""🧠 Interview One-Liner (MEMORIZE)

“Decorators can intercept and modify a function’s return value, which is useful for post-processing model outputs.”"""

# 🟡 Example: REALISTIC Production-Style Version
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def standardize_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)

        if not isinstance(data, (list, tuple)):
            raise TypeError("Expected list or tule")
        if not data:
            logger.warning("Empty output received...")
            return []
        max_value = max(data)
        if max_value == 0:
            return data
        
        return [x / max_value for x in data]
    return wrapper

@standardize_output
def get_predictions():
    return [10, 20, 30, 100]
print(get_predictions())