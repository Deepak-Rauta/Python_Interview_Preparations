def remove_duplicate(lst):
    unique_elements = []
    for elements in lst:
        if elements not in unique_elements:
            unique_elements.append(elements)
    return unique_elements
lst = [10, 20, 40, 60, 20, 10]
result = remove_duplicate(lst)
print(result)