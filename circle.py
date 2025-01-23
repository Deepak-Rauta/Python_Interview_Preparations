# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def cal_area(self):
#         area =  math.pi * self.radius**2
#         return area
#     def cal_perimeter(self):
#         perimeter = 2 * math.pi * self.radius
#         return perimeter
# radius = float(input("Enter the radius of the circle:"))
# #create a circle objects
# circle = Circle(radius)
# area = circle.cal_area()
# perimeter = circle.cal_perimeter()
# print(f'The area of a circle is:{area:.2f}')    
# print(f'The perimeter of a circle is {perimeter:.2f}')



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def cal_area(self):
        area = self.length * self.width
        return area
    def cal_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter
length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))
rectangle = Rectangle(length, width)
area = rectangle.cal_area()
perimeter = rectangle.cal_perimeter()
print(f'The area of a rectangle is:{area:.2f}')    
print(f'The perimeter of a rectangle is {perimeter:.2f}')




