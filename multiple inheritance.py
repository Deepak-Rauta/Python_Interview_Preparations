# In multiple inheritance there is one child class and more parent class
class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f'The name is:{self.name}')    

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f'The dance is:{self.dance}')    

class DancerEmp(Employee, Dancer):
    def __init__(self, dance, name):
        self.name = name
        self.dance = dance

o = DancerEmp('kathak', 'Nita')
print(o.name)
print(o.dance)
o.show() #if i do that then the first self.name will print
print(DancerEmp.mro())

# MRO - method resolution order



