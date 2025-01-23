# super keyword in python is used to refer the parent class
class parentClass:
    def parent_method(self):
        print('This is a parent method')
class childClass(parentClass):
    def parent_method(self):
        print('Deepak')
        super().parent_method()  # It will call the parent method
    def child_method(self):
        print("This is a child method")
#we call the parent class of parent method        
        super().parent_method()  # call the parent class of parent method
child_obj = childClass()  # To make a objects of child class
child_obj.child_method()
child_obj.parent_method()   # if we write this then it first print the deepak then it will print This is a parent method
# Because there will a parent method in child class so...it will print deepak