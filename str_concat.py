# Question:
# Concatenate "Hello" and "World" with a space in between.

str1 = "Hello"
str2 = "World"
result = str1 +" "+ str2
print(result)

# # Question:
# # Given ["Python", "is", "awesome"], concatenate all elements into a single string with spaces.

str = ["python", "is", "awesome"]
result = " ".join(str)
print(result)

# Question:
# Concatenate "The year is " and 2025.

# year = 2025
# result = "The year is" +" "  +str(year)
# print(result)

# Question:
# Concatenate "My name is" with "Alice" using .format()

name = "Deepak"
result = "My name is {}".format(name)
print(result)

# Question:
# Given first = "Good" and second = "Morning", concatenate them using f-strings.

first = "Good"
second = "Morning"
result = f"{first} {second}"
print(result)

# Question:
# Repeat "Hello " three times and concatenate "World!" at the end.

result = ("Hello " * 3) + "World!"
print(result)

# Question:
# Take two inputs from the user and concatenate them with a comma in between.
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# result = str1 + " " + str2
# print(result)


# Question:
# Given ["apple", "banana", "cherry"], concatenate them using " - " as a separator.

fruits = ["apple", "banana", "orange"]
result = " - ".join(fruits)
print(result)

# Question:
# Concatenate "Welcome" and "Home" without using +.

str1 = "Welcome"
str2 = "Home"
result = "{} {}".format(str1, str2)
print(result)

# Question:
# Convert [1, 2, 3, 4, 5] into "12345" without spaces.

numbers = [1,2,3,4,5]
result = "".join(str(num) for num in numbers)
print(result)










# import turtle
# t = turtle.Turtle()
# t.speed(3)
# turtle.bgcolor("black")
# t.pencolor("red")
# t.width(4)

# t.begin_fill()
# t.fillcolor("red")

# t.left(140)
# t.forward(180)
# t.circle(-90, 200)
# t.left(120)
# t.circle(-90, 200)
# t.forward(180)
# t.end_fill()

# t.penup()
# t.goto(-30, 50)
# t.pencolor("white")
# t.write("I ❤️ YOU Baby", font=("Arial", 24, "bold"))

# t.hideturtle()
# turtle.done()



# import turtle
# t = turtle.Turtle()
# t.speed(3)
# turtle.bgcolor("black")

# colors = ["red", "magenta", "violet", "purple"]

# t.width(3)
# t.penup()
# t.goto(0, -100)
# t.pendown()

# for color in colors:
#     t.pencolor(color)
#     t.fillcolor(color)
#     t.begin_fill()
#     t.left(140)
#     t.forward(180)
#     t.circle(-90, 200)
#     t.left(120)
#     t.circle(-90, 200)
#     t.forward(180)
#     t.end_fill()
#     t.penup()
#     t.goto(0, -100)
#     t.pendown()

# t.penup()
# t.goto(-40, 60)
# t.pencolor("white")
# t.write("You are my ❤️", font=("Arial", 20, "bold"))
# t.hideturtle()
# turtle.done()



