# list are a container to store the data
# fruits = ['Aplle', 'Banana', 'Orange', 5, 40.98, False]
# fruits[0] = "Apple"
# print(fruits[0])
# print(fruits[0:3])

# a = "Deepak"
# a[3] ='p'
# Here we can not change the string like this cz string are immutable 
# We change the string to another string in list
#list are mutable

## List Methods ##

# append() -->
fruits = ['Aplle', 'Banana', 'Orange', 5, 40.98, False]
fruits.append(True)
print(fruits)

# sort() -->
l1 = [10, 50, 40, 20, 30]
l1.sort()
print(l1)

# reverse() -->
l1 = [20, 40, 60, 70, 90]
# l1.reverse()
# print(l1)

# insert() -->
l1.insert(2, 50)
print(l1)
