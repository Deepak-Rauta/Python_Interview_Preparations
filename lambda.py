# # def appl(fx, value):
# #     return 6 + fx(value)

# # double = lambda x: x*2
# # print(double(5))

# # cube = lambda x: x**3
# # print(cube(5))

# # avg = lambda x,y,z: (x+y) / z
# # print(avg(2,6,4))

# # print(appl(lambda x: x*x, 2))

# def sum(n):
#     return (n+10)
# print(sum(10))

# # pattern-1 
# # function with one arguments
# # syntax: lambda <arg name> : <return statement>

# add = lambda n : n + 10
# print(add(20))

# # function with two arguments:

# summ = lambda n1,n2 : n1+n2
# print(summ(30,10))

# sqr = lambda i : i ** 2
# print(sqr(2))

# avg = lambda n1,n2,n3 : round((n1+n2+n3) / 3,2)
# print(avg(103,27,30))

# # if-else
# # lambda with if-else

# def greater(n1, n2):
#     if n1 > n2:
#         return (n1)
#     else:
#         return (n2)
# greater(10, 20)

# # syntax---->
# # func_name = lambda atr1, arg2 : <if-output> <if-condition> else <else-output>

# greater = lambda n1, n2 : n1 if n1 > n2 else n2
# print(greater(30, 40))

# # using list

# lst = [1,2,3,4,5]
# sq_lst = []
# for i in lst:
#     sq_lst.append(i ** 2)
# print(sq_lst)

# # sq_lst = [i ** 2 for i in lst]
# # print(sq_lst)

# list(map(lambda i : i ** 2, lst))
# print(sq_lst)

# # syntax---->
# # lambda <variable> : <op> <iterable>

# sq_lst = lambda i : i ** 2
# print(sq_lst(3))

# Example------>
numbers = [1,2,3,4,5,6,7,8]
# function to square of a number:
def square(x):
    return x ** 2
# using map function to apply the square function to each item in the number list 
squared_number = map(square, numbers)

# convert the map object to the list to see the result
print(list(squared_number))


# map()------>
# Defination:
# The map function in python allows you to apply a function to each item in an iterable(like a list)
# if we don't us ethe map function we will write a loop to achieve the result 
# that make the code longer as well

# without map function:----->

fahrenheit_temps = [32, 68, 77, 104]
celsius_temps = []

for temp in fahrenheit_temps:
    celsius = (temp - 32) * 5/9
    celsius_temps.append(celsius)

print(celsius_temps)  # Output: [0.0, 20.0, 25.0, 40.0]

# with map----->
fahrenheit_temps = [32, 68, 77, 104]

celsius_temps = list(map(lambda temp: (temp - 32) * 5/9, fahrenheit_temps))

print(celsius_temps)  # Output: [0.0, 20.0, 25.0, 40.0]

# filter ----->
# filter applies a function to each item of an iterable and return only 
# tnose items for wich the function returns 'True'

# Examples---->
# Suppose you want to filter out only the even numbers from a list.
numbers = [1,2,3,4,5,6]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)

l1 = ['hyd','mum#bai','che#nnai']
result = list(filter(lambda i : '#' in i, l1))
print(result)

# reduce
# reduce applies a function to the first two elements of an iterable 
# then cobine that result with the next elements and so on,
# until the iterable is reduced to a single value.
# Example--->
from functools import reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x, y : x * y, numbers)
print(product)

# without reduce----->

numbers = [1,2,3,4,5]
result = 1
for num in numbers:
    result *= num
print(result)

import functools
lst = [1,2,3,4,5]
print(functools.reduce(lambda s, i: s+i, lst,100)) # bydefault it takes zero summ = 0
# now summ starts from 100 

# without reduce 
lst = [1,2,3]
summ = 0
for num in lst:
    summ = summ + num
print(summ)


import functools as ft
lst = [1,2,3,4,5]
print(ft.reduce(lambda s, i: s+i, lst,100))