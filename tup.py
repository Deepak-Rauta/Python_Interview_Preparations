box_dimensions = (5, 3, 2)
length, width, height = box_dimensions
volume = length * width * height
print("Volume of the box:", volume)


try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the specific exception
    print("Error: Cannot divide by zero.")
