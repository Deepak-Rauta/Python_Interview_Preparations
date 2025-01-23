# Enumereate function in python is a built-in function that makes is easy to loop over a list 
# and keep track of both the index and the value of each item in the list
marks = [12, 56, 32, 98, 24, 76]
# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("I am a good boy!")
#     index = index + 1

# using enumerete---->

for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Deepak, is a good boy!")