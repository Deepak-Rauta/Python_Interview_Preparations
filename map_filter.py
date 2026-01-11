# Part 3: map() and filter()

"""1. The Intuition
map(function, list): "Apply this change to every item.
    "Analogy: You are a factory line. You stamp a logo on every single box passing by. 10 boxes in $\rightarrow$ 10 stamped boxes out.

filter(function, list): "Keep only the items that pass this test.
    "Analogy: You are a security guard. You only let people in who have a badge. 10 people try $\rightarrow$ Only 3 get in."""

# Map Example:
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# Filter Example:
nums = [1, 2, 3, 4]
# Keeps ionly even number
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

"""📝 Practice Problems: Map & Filter
Problem 1 (Easy - Map): You have a list of prices in dollars: prices = [100, 200, 300]. Use map and a lambda to convert them to Euros (assume 1 Dollar = 0.85 Euros). Return a list."""
prices = [100, 200, 300]
coverted_price = list(map(lambda x: x * 0.85, prices))
print(coverted_price)

"""Problem 2 (Easy - Filter): You have a list of ages: ages = [12, 35, 80, 14, 22]. Use filter and a lambda to keep only the people who are adults (18 or older). Return a list."""

ages = [12, 35, 80, 14, 22]
result = list(filter(lambda x: x >= 18, ages))
print(result)

"""Problem 3 (Medium - Map + String methods): You have a list of messy names: names = [" john ", " ALIce", "BOB "]. Use map to clean them up: strip whitespace and convert to Title Case (e.g., "John")."""

names = [" john ", " ALIce", "BOB "]
correct_order = list(map(lambda x: x.strip().title(), names))
print(correct_order)

"""Problem 4 (Medium - Filter + None): You have a list containing valid data and missing values: data = [10, None, 20, None, 50]. Use filter to remove the None values. Hint: lambda x: x is not None."""

data = [10, None, 20, None, 50]
filtered_result = list(filter(lambda x: x is not None, data))
print(filtered_result)

"""Problem 5 (Hard - Chaining): This is a real Data Science pipeline task! data = [1, 2, 3, 4, 5, 6]

Filter to keep only even numbers.

Map to square those numbers.

Return the final list. Hint: You can put filter() inside map()."""
data = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x **2, filter(lambda x: x % 2 == 0, data)))
print(result)


# 🎤 The Mock Interview

"""Interview Question:

"I have a list of dictionaries representing transactions. Some transactions are missing the 'amount' key (dirty data).

Write a function called clean_and_sum that:

Accepts a list of transaction dictionaries.

Filters out any transaction that is missing the 'amount' key.

Maps the remaining transactions to extract just the amount values.

Returns the Sum of those amounts.

Constraint: Try to use map, filter, and lambda where appropriate."""

def clean_and_sum(transactions):
    # Step 1: Filter transactions that have 'amount'
    valid_transactions = filter(lambda t: 'amount' in t, transactions)

    # step 2: Extract the amoun values
    amounts = map(lambda t: t['amount'], valid_transactions)

    # step 3: sum the amounts
    return sum(amounts)

transactions = [
    {"id": 1, "amount": 100},
    {"id": 2},                # Missing amount!
    {"id": 3, "amount": 50}
]

print(clean_and_sum(transactions))


