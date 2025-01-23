# Nested function
# def outer(x):
#     def inner(y):
#         return x+y
#     return inner
# f = outer(5)
# print(f(3))

# outer function return the inner function 
# The purpose of outer is to create and return a new function (inner) that has access to the variable x in its enclosing scope.
# if we wrote like return outer then it calling the outer function itself

# import random
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
# x_input = eval(input("Enter the number:"))
# f = outer(x_input)
# random_number = random.randint(1, 5)
# print(f(random_number))


# Multiple nested function-->
# import random
# def outer(x):
#     def middle(y):
#         def inner(z):
#             return x+y+z
#         return inner
#     return middle
# x_input = eval(input("Enter the number:"))
# f = outer(x_input)
# y_input = eval(input("Enter the number:"))
# h = f(y_input)
# random_number = random.randint(1, 5)
# print(h(random_number))

# Accessing Enclosing Variables:---->
# def outer(x):
#     y = 3
#     def inner(z):
#         return x+y+z
#     return inner
# f = outer(4)
# print(f(2))

def outer(x):
    y = 5
    def inner():
        nonlocal y
        y += x
        return y
    return inner

f = outer(10)
print(f())
print(f())
