# # class method
# class Employee:
#     company = 'Google'
#     def show(self):
#       print(f'The name is {self.name} and the company name is {self.company}')

# ## We also known if we make a method is also made for instance not class
#     @classmethod  ## if we want to self is refered to class then we use @classmethod 
#     def changeCompany(self, newCompany): ## This function also helps to change the company names
#        self.company = newCompany   ## it behaves like a normal function

# ## when we write classmethod decorator first of all it takes a first arguments as cls       


# e1 = Employee()  ## we make instance of a class here 
# e1.name = "Deepak"
# e1.show()
# e1.changeCompany('Microsoft')
# e1.show()
# print(Employee.company)


# class Employee:
#     company = 'TCS'
#     def show(self):
#       print(f'the name is {self.name} and the company name is {self.company}')
#     #
#     @classmethod
#     def changeCompany(self, newCompany):
#       self.company = newCompany

# c1 = Employee()
# c1.name = 'Deepak'
# c1.show()
# c1.changeCompany('cognizent')
# c1.show() 
# print(Employee.company)     


class Employee:
    company = "Tech mahindra"
    def show(self):
        print(f'The name is {self.name} and the company name is {self.company}')
    @classmethod
    def ChangeCompany(self, newCompany):
        self.company = newCompany

c1 = Employee()
c1.name = 'Deepak'
c1.show()     
c1.ChangeCompany("Accenture")
c1.show()
print(Employee.company)       

