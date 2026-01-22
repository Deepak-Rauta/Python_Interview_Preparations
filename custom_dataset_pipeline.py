"""The Theory: Making Objects Behave Like Built-ins
1. The Dataset Duo: __len__ and __getitem__
In Data Science, we rarely load all data into RAM at once (imagine a 1TB image dataset). Instead, we create a "map-style" dataset object that holds the instructions on how to get data, rather than the data itself.

__len__(self):

Intuition: This defines "How big is this container?"

Behavior: It allows your object to work with the built-in len() function.

PyTorch Context: The DataLoader needs this to calculate how many batches cover the epoch."""


"""__getitem__(self, index):

Intuition: This defines "Give me the item at specific position index."

Behavior: It allows your object to be indexed like a list: my_obj[5].

PyTorch Context: When training, the DataLoader generates a random index (e.g., 42) and calls dataset[42] to get that specific image/tensor."""


"""2. The Transformer: __call__
__call__(self, ...):

Intuition: This allows an instance of a class to be called as if it were a function.

Behavior: my_obj() executes the code inside __call__.

PyTorch Context: This is standard for Transforms. You define a class (e.g., Resize) with configuration in __init__, and the actual resizing logic in __call__. This keeps state (config) separate from action."""

"""Real-World Data Science Example
Let's build a mini-pipeline. We have a list of raw text sentences. We want a Dataset to hold them and a Transform to clean them."""


# --- Concept: __call__ (The Preprocessor) ---
class TextCleaner:
    def __init__(self, remove_punct=True):
        # We store configuration here
        self.remove_punct = remove_punct

    def __call__(self, text):
        # we perform the action here 
        if self.remove_punct:
            text = text.replace(".", "").replace("!", "")
        return text.lower().strip()

# --- Concept: __len__ & __getitem__ (The Dataset) ---
class SimpleTextDataset:
    def __init__(self, texts, transform=None):
        self.texts = texts
        self.transform = transform

    def __len__(self):
        # Allow len dataset
        return len(self.texts)
    
    def __getitem__(self, idx):
        # Allow dataset[idx]
        # 1. Fetch the raw data
        raw_text = self.texts[idx]

        # Apply transformation 
        if self.transform:
            raw_text = self.transform(raw_text)
        
        return raw_text

# ---USAGES---
raw_data = ["Hello World!", "Pytorch is fun.", "Good. Morning."]
# Initialize the transform (calls __init__)
cleaner = TextCleaner(remove_punct=True)

# Usage of __call__ -> looks like a function!
print(cleaner("TESTING...."))

# Initialize Dataset
dataset = SimpleTextDataset(raw_data, transform=cleaner)

# Usage of __len__
print(f"Dataset Size: {len(dataset)}") # Output: 3

# Usage of __getitem__
print(f"Item 1: {dataset[1]}") # Output: pytorch is fun

"""This code demonstrates how to build a basic Data Science pipeline using Python's "Magic Methods." It simulates how you would prepare data (like text) for a machine learning model."""

"""By writing transform=None, I am telling Python: "If the user doesn't provide a transform tool, just set this variable to None."""


# Problem:-1

"""Problem 1: Create a class SquaredNumbers.
__init__: Accepts a list of numbers.
__len__: Returns the count.
__getitem__: Returns the square of the number at that index."""

class SquaredNumber:
    def __init__(self, nums):
        self.nums = nums
    
    def __len__(self):
        return len(self.nums)
    
    def __getitem__(self, idx):
        current_num = self.nums[idx]
        return current_num ** 2

# Create instance with some data
my_numbers =SquaredNumber([2, 3, 5, 10])

# Use len()
print(f"Count: {len(my_numbers)}")

# Use indexing
print(f"Index 0 (2 squared): {my_numbers[0]}")
print(f"Index 3 (10 squared): {my_numbers[3]}")

# Problem-1.5
"""You are building a dataset for a weather prediction model. The raw data is in Celsius, but the model expects Fahrenheit.

Task: Create a class TemperatureDataset.

__init__: Accepts a list of temperatures in Celsius (e.g., [0, 100, -40]).

__len__: Returns the count of readings.

__getitem__: Returns the temperature converted to Fahrenheit.

Formula: (celsius * 1.8) + 32"""

class TemperatureDataset:
    def __init__(self, celcius):
        self.celcius = celcius

    def __len__(self):
        return len(self.celcius)
    
    def __getitem__(self, idx):
        fahrenheit_temp = self.celcius[idx]
        return (fahrenheit_temp * 1.8) + 32
    
temps = TemperatureDataset([0, 100])
print(temps[0])
print(temps[1])