def display_array(arr):
    print("Current Array:", arr)

def insert_element(arr, element, position):

    arr.insert(position, element)
    display_array(arr)

def delete_element(arr, element):
    if element in arr:
        arr.remove(element)
        display_array(arr)
    else:
        print(f"{element} not found in the array.")

def update_element(arr, old_element, new_element):
    if old_element in arr:
        index = arr.index(old_element)
        arr[index] = new_element
        display_array(arr)
    else:
        print(f"{old_element} not found in the array.")

def search_element(arr, element):
    if element in arr:
        print(f"{element} found at index {arr.index(element)}.")
    else:
        print(f"{element} not found in the array.")

# Example Usage
my_array = [1, 2, 3, 4, 5]

display_array(my_array)

insert_element(my_array, 10, 2)

delete_element(my_array, 3)

update_element(my_array, 2, 20)

search_element(my_array, 5)






