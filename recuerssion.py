# recurssion is the process of defining something in terms of itself
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# # number = int(input("Enter the number:"))
# # factorial = fact(number)
# print(fact(5))


## here we call the same function inside a function

# 5 * fact(4)
# 5 * 4 fact(3-1)
# 5 * 4 * 3 fact(2-1)
# 5 * 4 * 3 * 2 fact(1) in this case we get the error 
##  the error is in the fact(1) we got the vale 1


## fibonacci series:  0, 1, 1, 2, 3, 5, 8, 13, 21

def Fibonacci(n):
    if n < 0:
        print("Incorrect")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(5))


# # def Fibonacci(n):
 
# #     # Check if input is 0 then it will
# #     # print incorrect input
# #     if n < 0:
# #         print("Incorrect input")
 
# #     # Check if n is 0
# #     # then it will return 0
# #     elif n == 0:
# #         return 0
 
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
 
 
# # Driver Program
# print(Fibonacci(9))