from functools import wraps
import logging

logger = logging.getLogger(__name__)

def standardize_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)

        if not isinstance(data, (list, tuple)): # check what types of data something is?
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

# 🔹 STEP 1: Python reads the decorator function (NO execution yet)
def standardize_output(func):
# ✔ Python creates a function called standardize_output
# ❌ Nothing inside runs yet

# 🔹 STEP 2: Python reads get_predictions
# @standardize_output
# def get_predictions():
#     return [10, 20, 50, 100]

# ⚠️ This is IMPORTANT.

# This line is NOT just defining a function.
# It actually means:
# get_predictions = standardize_output(get_predictions)

# 🔹 STEP 3: Calling standardize_output(get_predictions)
# standardize_output(func=get_predictions)

# 3.1 wrapper function is CREATED
# def wrapper(*args, **kwargs):
    ...
# ✔ wrapper remembers func
# ✔ func = original get_predictions
# This memory is called a closure.

# 3.2 return wrapper
# return wrapper
# So now:
# get_predictions = wrapper
# 🚨 Original get_predictions is wrapped, not deleted.


# 🔹 STEP 4: Memory picture (CRUCIAL)
# get_predictions  ──► wrapper
#                         |
#                         └── func ──► original get_predictions

# 🔹 STEP 5: print(get_predictions())
# wrapper()
# Because get_predictions now points to wrapper.
# 🔹 STEP 6: Inside wrapper()
# 6.1 Call original function
# data = func(*args, **kwargs)
# 
#Calls:-
# original get_predictions()
# Which returns:
# [10, 20, 50, 100]
# So now:
# data = [10, 20, 50, 100]
# 6.2 Type check
# if not isinstance(data, (list, tuple)):
# data is a list ✅

# Condition is False

# Python skips the raise TypeError
# 6.3 Empty check
# if not data:
# List is NOT empty

# Condition is False

# Python continues
# 6.4 Find max value
# max_val = max(data)
# max_val = 100
# 6.5 Normalize the values
# [x / max_val for x in data]
# 10 / 100 = 0.1
# 20 / 100 = 0.2
# 50 / 100 = 0.5
# 100 / 100 = 1.0
# Result:
# [0.1, 0.2, 0.5, 1.0]

# 
# 
# 
# 
# 
# 
# 
# 
# 
#  