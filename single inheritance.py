class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
  def makeSound(self):  
    print("Animal are making sound")

class Dog(Animal): # we inherit the class
  def __init__(self, name, breed):
    Animal.__init__(self, name, species ='Dog')
    self.breed = breed
  def makeSound(self): # We override the method here
    print('Bark!')

d = Dog('Fido', 'Labrador')  
d.makeSound()

a = Animal('Fido', 'Dog')
a.makeSound()


# The inheritance in which a single derived class is inherit from a single base class is know as single inheritance

class Animal:
  def __init__(self, name, species):
    self.name = name 
    self. species = species
  def makeSound(self):
    print("Animal are making sound")

class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species = "Dog")
    self.breed = breed
  def makeSound(self):
    print('Bark!')

d = Dog('Fido', 'Labrador')
d.makeSound()

a = Animal('Fido', 'Dog')
a.makeSound()
