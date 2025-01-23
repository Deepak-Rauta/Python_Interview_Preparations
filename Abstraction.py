# Abstraction is the concept of hiding complex details and showing only the necessary part of the objects
# Purpose: Simplifies code and reduces complexity by focusing on the essential features.

# An abstract method is a method declared in a base (parent) class, but it doesn't have any implementation in that class.
# It is meant to be overridden by subclasses. The base class that contains the abstract method cannot be instantiated (you can't create objects of it).
from abc import ABC, abstractmethod
# Abstract base class
class Animal(ABC):
    @abstractmethod
    def sound(self):  # abstract method
        pass # No implemantaion, subclasses must define this class
# subclass dog, implementing the abstract method
class dog(Animal):
    def sound(self):
        return "bark"
class cat(Animal):
    def sound(self):
        return "meow"

# creating the instance of dog and cat
d = dog()
c = cat()

print(d.sound())
print(c.sound())


