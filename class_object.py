class person:
    name = "Deepak"
    occupation = "Data Scientist"
    salary = 40000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

# now create object 
a = person()
b = person()
c = person()

# a.name = "Nita"
# a.occupation = "Teacher"

b.name = "Bikash"
b.occupation = "Air force"

c.name = "Roshan"
c.occupation = "navy"

# print(a.name, a.occupation)

a.info()
b.info()
c.info()


# self() ------->
# self keywords generally used to refer the current instance of the class 
# It allows you to access variables and methods that belongs to the class
# self refer to the current object 


class car:
    def __init__(self, model, color):
        self.model = model 
        self.color = color
    
    def display(self):
        print(f"The car model is: {self.model} and the color is: {self.color}")
# now we create object 
my_car = car("BMW", "Black")
my_car.display()



# Q1
class person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"{self.name} has {self.age} years old and he is a {self.gender}")
    def is_adlut(self):
        return self.age >= 18
s = person("Deepak", 22, "Male")
s.introduce()
print(s.is_adlut())
