# a = input("Enter the number:")
# print(f'The multiplication table of {a} is:')
# try:
#   for i in range(1, 11):
#     print(f'{int(a)} X {i} = {int(a)*i}')
# except Exception as e:  # we can write also except
#   print(e)    # it will print the eror invalid literal for int()
# After that it will excecute the next line  


# print("Some important lines of code")
# print("The end of code")    



# # Exception handling ->Exception handling basically deal with error that may occer during the excecution of a program
# # Basic try-exception code
# try:
#   result = 10/0    # this will rise a zeroDivision error
# except ZeroDivisionError:
#   print("Error: can not devide by zero")


# # Handling multiple exception
# try:
#     value = int("abc")  # This will raise a ValueError
# except ValueError as e:
#     print(f"Error: {e}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")



# using else block
# try:
#    Result = 10 / 2
# except ZeroDivisionError:
#    print('can not devide by zero')
# else:
#    print('The result is', Result)      


##finally block --> the finally block excecuted whether the exception is occer or not
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# finally:
#     print("This will always execute.")

# try:
#    l = [1,2,3,4,6]
#    i = int(input("Enter the index:"))
#    print(l[i])
# except:
#   print("Some error occured")
# finally:
#   print("It will excute")

# try:
#   result = 10 / 0
# except ZeroDivisionError:
#   print("Can not divided by zero!")
# finally:
#   print("It will excecute as well!")

## Exception handling --->

# def my_func(a,b):
#   try:
#     result = a / b
#     return result
#   except ZeroDivisionError as e:
#     print(e)
#     print("It can not divided by zero")
# x = my_func(2, 0)
# print(x)

# Multiple exception------->
# def my_prog(lst, index):
#     try:
#         if lst is None:
#             raise ValueError("The list is none")
#         element = lst[index]
#         return element
#     except IndexError as e:
#         print(f"Indexerror: {e}")
#         print(f"The index {index} is out of range")
#     except ValueError as e:
#         print(f"ValueError : {e}")
#     except Exception as e:  # it catches any other unexpected exception
#         print(f"An unexpected error occured: {e}")
#     finally:
#         print("This code is run as well!")
# #print(my_prog([1,2,3,4], 5))  # The index is out of range
# print(my_prog(None, 1))  # List is none 

# Nested Try-Except----------->
# def my_code(n1, n2):
#     try:
#         try:
#             result = n1 / n2
#             return result
#         except TypeError as e:
#             print(f"TypeError: {e}")
#             print("Make sure that both input have numbers")
#     except ZeroDivisionError as e:
#         print(f"ZeroDivisionError: {e}")
#         print("A number can not divided by zero")
#     except Exception as e:
#         print(f"An unexpected error is occured as {e}")         

# #print(my_code('deepak', 5))
# print(my_code(10, 0))
# #print(my_code(10, 2))


# Custom Exception handling ---->>
# Custom exception handling in simple words is when you create your own error types in Python, instead of just using the built-in ones like ValueError or TypeError.

# custom exception are typically created using classes 

def check_positive_number(num):
    if num < 0:
        raise ValueError(f"Invalid input: {num}, The number can not be negetive")
    else:
        return f"The number {num} is positive!"

print(check_positive_number(10))      
#print(check_positive_number(-1))      





  



