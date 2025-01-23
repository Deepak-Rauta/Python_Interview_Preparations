#For loop with else

# for i in range(5):
#     print(i)
# else:
#     print("sorry")    


# if we create a empty list then it directly jump to the empty else part

# for i in []:
#     print(i)
# else:
#     print("sorry")

# for i in range(6):
#     print(i)
#     if i == 4:
#         break
# else:
#     print("sorry")


# i = 0
# while i <6:
#     print(i)
#     i=i+1
#     # if i == 5:
#     #     break
# else:
#     print("Good morning!")


# for x in range(5):
#     print("Iteration no {} in for loop".format(x+1))
    
# else:
#     print("else block in loop")
# print("out of loop")

# The format() method in python is used to format the string 
# Examples:-

# name="deepak"
# age = 21
# message = "Hello my name is {} and i am {} years old".format(name, age)
# print(message)

# my_list = [1,2,3,4,5,6,7]
# target = 3
# for i in my_list:
#     print(i)
#     if i == target:
#         print(f"found the target:{target}")
#         break
# else:
#     print(f"The target {target} is not found!")


i = 0
my_list = [1,2,3,4,5,6,7]

while i < len(my_list):
    if my_list[i] == 3:
        print("I go the target")
        
        break
    i = i+1
else:
    print("I am not gpt the target")





# count = 5
# while count > 0:
#     print(f"count: {count}")
#     count = count-1
# else:
#     print("count down finished!")


count = 5
while count > 0:
    print(f"count: {count}")
    if count == 7:
        print("breaking the loop")
        break
    count = count - 1
else:
    print("countdown finished")