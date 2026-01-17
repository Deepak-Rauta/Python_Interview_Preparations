# Defining the class
class DataPoint:
    pass  # 'pass' just means 'do nothing', its a placeholder

# 2. creating an object
point_a = DataPoint()
point_b = DataPoint()

# 3. Adding Data (Furniture) to a specific object
# In Python, you can stick variables onto objects dynamically (though we usually use __init__)

point_a.x = 10
point_a.y = 20
print(point_a.x) # Output: 10


"""Problem 1: The Empty Container Define a class named ModelEvaluator. It should be empty (use pass). Create an instance of this class and assign it to a variable named evaluator."""

class ModelEvaluator:
    pass 

evaluator = ModelEvaluator()

"""Problem 2: Dynamic Attributes Using the evaluator object you just created, manually assign an attribute named accuracy with the value 0.95. Print the accuracy."""

class ModelEvaluator:
    pass 

evaluator = ModelEvaluator()
evaluator.accuracy = 0.95
print(evaluator.accuracy)

"""Problem 3: Distinct Instances Create a class Dataset. Create two separate instances: train_data and test_data. Manually assign an attribute rows to train_data with value 1000. Manually assign an attribute rows to test_data with value 200. Print the rows attribute for both to prove they are storing data separately."""

class Dataset:
    pass

train_data = Dataset()
test_data = Dataset()

# # Both use the SAME attribute name ('rows'), but store DIFFERENT data.
train_data.rows = 1000
test_data.rows = 200

print(train_data.rows)
print(test_data.rows)

"""Problem 4: Type Checking Using type(), print the type of your train_data object. Then, use isinstance() to check if train_data is an instance of the Dataset class."""

# Check the type of the object
print(type(train_data))

# Check if train data is actually a Dataset
is_dataset = isinstance(train_data, Dataset)
print(is_dataset)

"""Problem 5: Reference vs. Value (Tricky) Create a class Feature. Create an instance f1 = Feature(). Assign f2 = f1. Assign f1.name = "Age". Print f2.name. Explain in one sentence why f2 has a name, even though you only touched f1."""

class Feature:
    pass

f1 = Feature()
f2 = f1

f1.name = "Age"
print(f2.name)

"""Feedback on your explanation: You are very close, but there is a subtle distinction that is critical for interviews. You said: "all the property and methods of f1 now stored in f2".

In Python, f2 = f1 does not create a copy. It does not store f1's stuff inside f2. Instead, f1 and f2 are just two different nametags stuck to the exact same box.

If you burn the box using the name f1, the box labeled f2 is also burnt—because it's the same box.

This is called Pass by Reference (or assignment by reference)."""

# Module 2: __init__ and self

# Now we address the annoyance of Module 1. In Module 1, we had to do this:
# p = Point()
# p.x = 10  # Tedious manual assignment
# p.y = 20
"""If we forget to set .x, our code crashes later. We need a way to force data to be set the moment the object is created. This is the Constructor (__init__)."""

"""1. The Intuition: __init__
Think of __init__ as the Starter Kit. When you sign up for a gym (create an object), the receptionist (__init__) immediately gives you a key card and a towel. You cannot exist as a member without them.

2. The Intuition: self
This is the most confusing part for learners.

The Problem: The Class (Blueprint) is generic. It doesn't know about specific objects.

The Solution: When you create object_A, Python passes object_A into the code and calls it self.

self translates to: "This specific object we are building right now."""

# 3. Syntax & Data Science Example
class StandardScaler:
    # This runs AUTOMATICALLY when you do StandardScaler(...)
    def __init__(self, mean, std):
        self.mean = mean  # Attach 'mean' variable to THIS object
        self.std = std    # Attach 'std' variable to THIS object

# USAGE:
# Python sees this, creates a blank object, and passes it as 'self'
scaler_1 = StandardScaler(mean=50, std=10)
scaler_2 = StandardScaler(mean=0, std=1)

print(scaler_1.mean) # Output: 50
print(scaler_2.mean) # Output: 0

"""Key Takeaway:

self.mean = mean reads as: "Take the value mean passed by the user, and save it inside this object under the name mean."""

"""Problem 1: The Basics Create a class Student. Use __init__ so that every time a student is created, you must provide a name and a gpa. Create an instance s1 with name "Sam" and GPA 3.5. Print the GPA."""
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
s1 = Student(name="Sam", gpa=3.5)
print(s1.gpa)

"""Problem 2: Defaults Create a class NeuralNetwork. It should have an __init__ that takes layers. If the user doesn't provide layers, it should default to [10, 5, 1]. Create two instances: n1 (with layers [50, 50]) and n2 (using default). Print the layers for both."""

class NeuralNetwork:
    # We set the default value right here in the arguments
    def __init__(self, layers=[10, 5, 1]):
        self.layers = layers
# n1: We provide specific layers, so the default is ignored
n1 = NeuralNetwork(layers=[50, 50])    
# n2: We provide nothing, so Python uses [10, 5, 1]
n2 = NeuralNetwork()
print(n1.layers)
print(n2.layers)

"""Problem 3: The "Self" Trap (Fix the Bug) Look at this broken code. It runs without error, but print(model.lr) fails. Please write the corrected version."""
class Model:
    def __init__(self, lr):
        self.lr = lr  # <--- ERROR IS HERE: This variable dies when __init__ finishes

model = Model(lr=0.01)
print(model.lr)

"""Problem 4: Logic inside Init Create a class Discount. It takes a value (float). Inside __init__, write logic: if value is greater than 1.0, set self.value to 1.0 (cap it). Otherwise, set it to the provided value. Test it with d = Discount(1.5). Print d.value (should be 1.0)."""

class Discount:
    def __init__(self, value):
        # we check the input before saving it to the object
        if value > 1.0:
            self.value = 1.0
        else:
            self.value = value

# Test 1: value is too high, gets capped
d = Discount(1.5)
print(d.value)

d2 = Discount(0.8)
print(d2.value)


"""Problem 5: Data Science Context Create a class DataFrameInfo. Its __init__ takes a list of column names (e.g., ['age', 'salary']). Inside __init__, create an attribute self.n_cols that automatically calculates and stores the length of that list. Create an instance with 3 column names and print n_cols."""

class DataFrameInfo:
    def __init__(self, columns):
        # We store the list itself
        self.columns = columns

        # we also calculate and store metadata about the list immediately
        self.n_cols = len(columns)

# Usage
df_info = DataFrameInfo(['age', 'salary', 'geneder'])
print(df_info.n_cols)

"""Interview Problem 1: Input Validation
Scenario: You are building a class called TrainingJob. Requirements:

The __init__ method takes one argument: epochs (an integer).

If epochs is less than 1, force self.epochs to be 1 and print a warning message "Epochs must be >= 1. Resetting to 1."

Otherwise, set self.epochs to the provided value."""
# class TrainingJob:
#     def __init__(self, epochs):
#         self.epochs = epochs
#         if epochs < 1:
#             self.epochs = 1
#             print("Epochs must be >= 1. Resetting to 1")
# my_obj = TrainingJob(epochs=0.8)
# print(my_obj.epochs)

class TrainingJob:
    def __init__(self, epochs):
        if epochs < 1:
            print("Epochs must be >= 1. Resetting to 1.")
            self.epochs = 1
        else:
            self.epochs = epochs
job = TrainingJob(epochs=0)
print(job.epochs)

"""Interview Problem 2: The Mutable Default Argument Trap (Crucial!)
This is the most common Python interview question.

Scenario: You want a class StudentGroup where you can add student names. The Bug: Look at the code below."""

"""Why did group_b inherit Alice?? Because in Python, default lists [] are created once when the function is defined, not every time you call it. All objects share that same list!

The Task: Rewrite the __init__ method to fix this bug so that group_a and group_b do not share the same list. (Hint: Use None)"""

# Mutable Default Argument Trap.

class StudentGroup:
    def __init__(self, students=None):
        if students is None:
            self.students = [] # create a NEW list for this specific object
        else:
            self.students = students
# Usage:-
group_a = StudentGroup()
group_a.students.append("Alice")

group_b = StudentGroup()
# group_b creates its OWN fresh list, so it is empty
print(group_b.students)


"""Interview Problem 3: String Parsing in Init
Scenario: You are processing user data. The input comes in as a single string "Firstname Lastname". The Task: Create a class User.

The __init__ takes a single string full_name.

Inside __init__, split this string to create two separate attributes: self.first and self.last.

Assume the string always has exactly one space (e.g., "Elon Musk").

Test it with u = User("Elon Musk") and print u.first."""

class User:
    def __init__(self, full_name):
        # We process the data right here inside the constructor
        # "Elon Musk".split(" ") becomes ["Elon", "Musk"]
        name_parts = full_name.split(" ")

        self.first = name_parts[0]
        self.last = name_parts[1]

# Usage
u = User("Elon Musk")
print(u.first)  # Output: Elon
print(u.last)   # Output: Musk      
