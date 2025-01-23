# Accenture previous year questions

# Functions should be determined minimum no. of houses required to provide enough food for all the rats

def min_house(r, unit, arr):
    # First calculate the total no. of foods
    total_food = r * unit
    # Initialize the variables to keep track of food and houses count
    food_gathered = 0
    house_count = 0
    for food in arr:
        food_gathered += food
        house_count += 1
    # check if we have enough food
        if food_gathered > total_food:
            return house_count
        # if all houses not enough
    return -1
r = 7
unit = 2
arr = [2,8,3,5,7]
result = min_house(r, unit, arr)
print(result)


