# getter and setter

# In python, getters and setter arer the methods used to access(get) or modify(set) the values of private or protected atributes of a class

# getter:
# retrive the value of an attributes 
# get_

# setter:
# set or update the value of an attributes


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



class person:
    def __init__(self, name, age):
        self.__name = name # Private attributes
        self.__age = age # private attributes

    # getter methods for name
    def get_name(self):
        return self.__name
    
    # setter methods for change the name
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print('Enter a valid age')
    
    # Getter method for get the age
    def get_age(self):
        return self.__age
    
# create an instance
obj = person('Nita', 22)

# Acessing the data using getter methods
print(obj.get_name())
print(obj.get_age())

# Acessing the data using setter methods 
obj.set_age(23)
print(obj.get_age())

