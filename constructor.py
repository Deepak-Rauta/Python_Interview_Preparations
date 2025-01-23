# # Constructor also helps to initialize the objects
# class person:
#     def __init__(self, name, occ):   # This method always call when we make a objects
#         print('Hey i am a constructor!')
#         self.name = name
#         self.occ = occ 
#     def info(self):
#         print(f'{self.name} is a {self.occ}')

# a = person('Deepak', 'Engineer') # create the instance
# a.info()
# b = person('Bikash', 'Airforce')  # Here self autometically pass
# # b.info()
# # #b = person()
# # # When we make a objects the constructor will be call
# # # print(a.name)
# # # a.name = 'Bikash'  # when we make this object there is no need to require the above name and occ
# # # a.occ = 'Airforce'
# # #a.info()  # call the info method    



class person():
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} has {self.occ}")
a = person("Biaksh", "Airfoce")
b = person("Roshan", "Navy")
#print(a.name)
a.info()
b.info()


