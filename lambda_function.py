# As a reminder, a lambda is a short, one-line function that you don't need to define using def.

"""Problem 1 (Easy):Write a lambda function assigned to a variable named multiply.It should take two arguments, x and y, and return their product (x * y)."""

multiply = lambda x, y: x * y
print(multiply(5, 3))

"""Problem 2 (Easy): String Manipulation

Write a lambda function assigned to get_last_char. It should take a single string s and return the last character of that string."""

get_last_char = lambda x: x[-1]
print(get_last_char("python"))

"""Problem 3 (Medium): Logic inside Lambda

Write a lambda function assigned to is_even. It should take one integer n and return True if the number is even, and False otherwise."""

is_even = lambda x: x%2 == 0
print(is_even(10))

"""Problem 4 (Medium): Sorting with Lambda

This is a classic interview question. You almost never write a sorting algorithm from scratch; you use sorted() with a "key"."""

users = [("Tom", 12), ("Alice", 30), ("Bob", 25)]
sorted_users = sorted(users, key=lambda x: x[1])
print(sorted_users)

"""If i don't write key=lambda x: x[1] (or if i write key=lambda x: x[0]), Python falls back to its default sorting behavior.

For tuples, the default behavior is "Alphabetical Order" based on the first item."""

"""Problem 5 (Hard): The "Factory" Pattern

Write a function power_factory(n). It should return a lambda function that raises x to the power of n.

Input: An integer n (the exponent).

Output: A function (not a number)."""

def power_factory(n):
    return lambda x: x ** n
square = power_factory(2)
print(square(5))
