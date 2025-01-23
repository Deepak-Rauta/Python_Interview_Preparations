# polymerphisim is a programming concept in python that allows the same function to be used for different types 

class Bird:
    def sound(self):
        return "Tweet"
class Dog:
    def sound(self):
        return "Bark"
def make_sound(animal):
    print(animal.sound()) # same methods works for different objects

bird = Bird()
dog = Dog()

make_sound(bird)
make_sound(dog)

# In the above code Bird and Dog both have sound() method and make_sound() can handle both objects without knowing their specific types

# Examples:------------->

class Person:
    def __init__(self, name, age):
        self.__name = name # private attributes
        self.__age = age # private attributes

    # Getter nmethod for name
    def get_name(self):
        return self.__name
    
    # setter method for change name
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("pls enter a valid age")

    # Getter method for get the age
    def get_age(self):
        return self.__age
    
# create an instance
person = Person("Nita", 22)

# Asscessing data using getter method
print(person.get_name())
print(person.get_age())

# Modifying data using setter method 
person.set_age(23)
print(person.get_age())